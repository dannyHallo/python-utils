import src.backup_and_recovery as backup_and_recovery


def exitSafely():
    exit(0)


def exitWithRecovery(project_path: str):
    backup_and_recovery.recover_original_version(project_path)
    exit(1)
