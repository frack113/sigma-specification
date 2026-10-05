# product: windows, service: windefend

```yaml
logsource:
    product: windows
    service: windefend
```

<!-- mdformat-toc start --slug=github --no-anchors --maxlevel=6 --minlevel=2 -->

- [Telemetry](#telemetry)
- [Points of Attention](#points-of-attention)
- [Fields](#fields)

<!-- mdformat-toc end -->

## Telemetry

- Channel: Microsoft-Windows-Windows Defender/Operational

## Points of Attention

- The rules set `definition: 'Requirements:Enabled Block process creations originating from PSExec and WMI commands from Attack Surface Reduction (GUID: d1e49aac-8f56-4280-b9ba-993a6d77406c)'`.

## Fields

The rules of this log source use the following field names:

- `EventID`
- `Feature_Name`
- `NewValue`
- `OldValue`
- `Path`
- `ProcessName`
- `Reason`
- `SourceName`
- `Value`
