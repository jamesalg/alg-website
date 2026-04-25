# Lock Register — ALG Website v2.0

Per Playbook v2.0 §9. A lock means: subsequent iterations cannot modify the listed path without an explicit `REOPEN: <Lock ID>` line in the prompt + James approval.

## Currently Locked

*(none — iteration 1 has not yet merged)*

## Lock Format

```
| Lock ID | Path                          | Locked at | Locked by | Reopen requires |
| L01     | example/path                  | v2.1.0    | James     | Explicit prompt |
```

## How locks get added

1. Iteration merges to `main`
2. Claude proposes lock candidates in the merge note
3. James confirms which paths to lock
4. Entry added here, dated, version-tagged

## How locks get removed (REOPEN)

1. New prompt includes `REOPEN: L<id>` for each lock to be touched
2. James explicit approval in the chat
3. Lock entry moved to "Reopened" section below with date and reason
4. After the reopening iteration merges, lock can be re-applied (with new Lock ID)

## Reopened Locks

*(none yet)*
