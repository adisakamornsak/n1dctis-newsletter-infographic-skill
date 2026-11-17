"""Exercise online-update behavior against a local Git remote, without GitHub writes."""
from contextlib import redirect_stdout, redirect_stderr
import io
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from tools import manage_skill as manager
from tools import package_skill as pack

ROOT = Path(__file__).resolve().parents[1]


class InstallUpdateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.remote = self.root / 'remote'
        self.source = self.remote / manager.NAME
        self.skills = self.root / 'user/skills'
        self.state = self.root / 'state'
        self.target = self.skills / manager.NAME
        for relative in pack.REQUIRED:
            p = self.source / relative
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text('fixture', encoding='utf-8')
        shutil.copyfile(ROOT / 'pea-newsletter-infographic/scripts/preflight_update.py',
                        self.source / 'scripts/preflight_update.py')
        self.version('v3.0.0')
        self.git('init', '--initial-branch=main')
        self.commit()

    def git(self, *args):
        return manager.command(['git', '-C', str(self.remote), '-c', 'user.email=test@example.invalid',
                                '-c', 'user.name=Fixture', *args])

    def version(self, value):
        (self.source / 'SKILL.md').write_text(
            f'---\nname: {manager.NAME}\ndescription: Test skill\n---\n# team edition {value}\n', encoding='utf-8')

    def commit(self):
        self.git('add', '--all')
        self.git('commit', '-m', 'fixture')

    def sync(self, **kwargs):
        with redirect_stdout(io.StringIO()):
            return manager.synchronize(self.skills, self.state, repo=str(self.remote), **kwargs)

    def install(self):
        return self.sync(installing=True)

    def snapshot(self):
        return {p.relative_to(self.target).as_posix(): p.read_bytes()
                for p in self.target.rglob('*') if p.is_file()}

    def test_install_preserves_remote_bytes_and_persists_updater(self):
        data = self.install()
        self.assertEqual(data['version'], 'v3.0.0')
        self.assertEqual(data['commit'], self.git('rev-parse', 'HEAD'))
        self.assertEqual((self.target / 'assets/pea-logo-exact-original.png').read_bytes(),
                         (self.source / 'assets/pea-logo-exact-original.png').read_bytes())
        self.assertTrue((self.state / 'manage_skill.py').is_file())
        self.assertTrue((self.state / 'package_skill.py').is_file())

    def test_update_fetches_new_commit_removes_retired_file_and_backs_up(self):
        (self.source / 'assets/retired.md').write_text('old')
        self.commit()
        self.install()
        before = self.snapshot()
        (self.source / 'assets/retired.md').unlink()
        self.version('v3.1.0')
        self.commit()
        data = self.sync()
        self.assertEqual(data['version'], 'v3.1.0')
        self.assertFalse((self.target / 'assets/retired.md').exists())
        backups = list((self.skills.parent / 'pea-newsletter-backups').iterdir())
        self.assertEqual(len(backups), 1)
        self.assertEqual((backups[0] / 'SKILL.md').read_bytes(), before['SKILL.md'])

    def test_same_version_new_commit_is_installed(self):
        first = self.install()
        p = self.source / 'assets/approved-layout-reference.jpg'
        p.write_bytes(b'new owner-maintained reference')
        self.commit()
        second = self.sync()
        self.assertEqual(first['version'], second['version'])
        self.assertNotEqual(first['commit'], second['commit'])
        self.assertEqual((self.target / p.relative_to(self.source)).read_bytes(), p.read_bytes())

    def test_same_commit_still_checks_remote_without_accumulating_backups(self):
        first = self.install()
        second = self.sync()
        self.assertEqual(first['commit'], second['commit'])
        self.assertNotEqual(first['checked_at'], second['checked_at'])
        self.assertEqual(list((self.skills.parent / 'pea-newsletter-backups').iterdir()), [])

    def test_local_edits_stop_update_and_explicit_reinstall_preserves_backup(self):
        self.install()
        p = self.target / 'SKILL.md'
        p.write_text(p.read_text() + 'local edit')
        before = self.snapshot()
        with self.assertRaisesRegex(ValueError, 'ไฟล์สกิลถูกแก้'):
            self.sync()
        self.assertEqual(self.snapshot(), before)
        self.sync(installing=True, replace_existing=True)
        backups = list((self.skills.parent / 'pea-newsletter-backups').iterdir())
        self.assertEqual(len(backups), 1)
        self.assertEqual((backups[0] / 'SKILL.md').read_bytes(), before['SKILL.md'])

    def test_unmanaged_install_requires_explicit_backup_and_replacement(self):
        self.target.mkdir(parents=True)
        (self.target / 'notes.txt').write_text('keep me')
        with self.assertRaises(ValueError):
            self.sync(installing=True)
        self.sync(installing=True, replace_existing=True)
        backups = list((self.skills.parent / 'pea-newsletter-backups').iterdir())
        self.assertEqual((backups[0] / 'notes.txt').read_text(), 'keep me')

    def test_network_failure_keeps_installed_copy_and_does_not_launch_codex(self):
        self.install()
        before = self.snapshot()
        self.remote.rename(self.root / 'offline')
        with patch.object(manager.subprocess, 'call') as launch, redirect_stderr(io.StringIO()):
            code = manager.main(['--skills-dir', str(self.skills), '--state-dir', str(self.state),
                                 'run', '--prompt', 'test'])
        self.assertEqual(code, 1)
        launch.assert_not_called()
        self.assertEqual(self.snapshot(), before)

    def test_invalid_upstream_asset_keeps_installed_copy(self):
        self.install()
        before = self.snapshot()
        (self.source / 'assets/pea-logo-exact-original.png').unlink()
        self.commit()
        with self.assertRaisesRegex(ValueError, 'Missing required files'):
            self.sync()
        self.assertEqual(self.snapshot(), before)

    def test_remote_symlink_is_rejected_without_touching_installation(self):
        self.install()
        before = self.snapshot()
        (self.source / 'assets/escape.md').symlink_to('/etc/passwd')
        self.commit()
        with self.assertRaisesRegex(ValueError, 'links'):
            self.sync()
        self.assertEqual(self.snapshot(), before)

    def test_replacement_failure_rolls_back(self):
        self.install()
        before = self.snapshot()
        self.version('v3.1.0')
        self.commit()
        original = Path.rename
        def fail_candidate(path, destination):
            if path.parent.name.startswith('.pea-stage-'):
                raise OSError('simulated disk failure')
            return original(path, destination)
        with patch.object(Path, 'rename', fail_candidate), self.assertRaises(OSError):
            self.sync()
        self.assertEqual(self.snapshot(), before)

    def test_simultaneous_update_is_rejected(self):
        self.state.mkdir()
        lock = self.state / '.update.lock'
        lock.mkdir()
        with self.assertRaisesRegex(RuntimeError, 'อัปเดตอื่น'):
            self.install()
        self.assertTrue(lock.exists())

    def test_preflight_updates_installed_skill_before_use(self):
        self.install()
        self.version('v3.2.0')
        self.commit()
        p = self.target / 'scripts/preflight_update.py'
        result = subprocess.run([sys.executable, str(p)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(manager.receipt(self.target)['version'], 'v3.2.0')

    def test_preflight_without_managed_installation_stops(self):
        result = subprocess.run([sys.executable, str(self.source / 'scripts/preflight_update.py')],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn('install', result.stderr)

    def test_run_checks_then_launches_new_session_with_prompt_and_images(self):
        self.install()
        self.version('v3.3.0')
        self.commit()
        seen = []
        def launch(cmd):
            seen.append(manager.receipt(self.target)['version'])
            self.assertEqual(cmd[:3], ['codex', '--image', 'news.jpg'])
            self.assertIn('$' + manager.NAME, cmd[-1])
            self.assertIn('ทดสอบข่าว', cmd[-1])
            return 7
        with patch.object(manager.subprocess, 'call', side_effect=launch), redirect_stdout(io.StringIO()):
            code = manager.main(['--skills-dir', str(self.skills), '--state-dir', str(self.state),
                                 'run', '--image', 'news.jpg', '--prompt', 'ทดสอบข่าว'])
        self.assertEqual(code, 7)
        self.assertEqual(seen, ['v3.3.0'])


if __name__ == '__main__':
    unittest.main()
