# product: windows, service: sysmon

```yaml
logsource:
    product: windows
    service: sysmon
```

<!-- mdformat-toc start --slug=github --no-anchors --maxlevel=6 --minlevel=2 -->

- [Description](#description)
- [Telemetry](#telemetry)
- [Points of Attention](#points-of-attention)
- [Fields](#fields)

<!-- mdformat-toc end -->

## Description

Events written by Sysmon when it blocks an operation or when its configuration is changed. The other events of Sysmon use the Sigma category that describes them, for example `category: file_event, product: windows`, with the fields of the Sysmon schema.

## Telemetry

Events written by Sysmon.

- Channel: Microsoft-Windows-Sysmon/Operational
- Sysmon events: SysmonConfigChange, FileBlockExecutable, FileBlockShredding, FileExecutableDetected

## Points of Attention

- Only the configuration changes of Sysmon and the operations it blocked or denied are written to this log source. The rules for the other Sysmon events use the category that describes the event.

## Fields

The rules of this log source use the following field names:

- `EventID`
