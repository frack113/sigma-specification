# product: windows, service: taskscheduler

```yaml
logsource:
    product: windows
    service: taskscheduler
```

<!-- mdformat-toc start --slug=github --no-anchors --maxlevel=6 --minlevel=2 -->

- [Telemetry](#telemetry)
- [Points of Attention](#points-of-attention)
- [Fields](#fields)

<!-- mdformat-toc end -->

## Telemetry

- Channel: Microsoft-Windows-TaskScheduler/Operational

## Points of Attention

- The rules set `definition: 'Requirements: The "Microsoft-Windows-TaskScheduler/Operational" is disabled by default and needs to be enabled in order for this detection to trigger'`. 3 rules use the same requirement.

## Fields

The rules of this log source use the following field names:

- `EventID`
- `Path`
- `TaskName`
- `UserName`
