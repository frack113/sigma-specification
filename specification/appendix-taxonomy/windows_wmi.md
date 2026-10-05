# product: windows, service: wmi

```yaml
logsource:
    product: windows
    service: wmi
```

<!-- mdformat-toc start --slug=github --no-anchors --maxlevel=6 --minlevel=2 -->

- [Telemetry](#telemetry)
- [Points of Attention](#points-of-attention)
- [Fields](#fields)

<!-- mdformat-toc end -->

## Telemetry

- Channel: Microsoft-Windows-WMI-Activity/Operational

## Points of Attention

- The rules set `definition: 'WMI Namespaces Auditing and SACL should be configured, EventID 5861 and 5859 detection requires Windows 10, 2012 and higher'`.

## Fields

The rules of this log source use the following field names:

- `EventID`
- `Operation`
- `PossibleCause`
- `Provider`
- `Query`
- `User`
