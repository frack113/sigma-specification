# product: windows, service: ntlm

```yaml
logsource:
    product: windows
    service: ntlm
```

<!-- mdformat-toc start --slug=github --no-anchors --maxlevel=6 --minlevel=2 -->

- [Telemetry](#telemetry)
- [Points of Attention](#points-of-attention)
- [Fields](#fields)

<!-- mdformat-toc end -->

## Telemetry

- Channel: Microsoft-Windows-NTLM/Operational

## Points of Attention

- The rules set `definition: 'Requires events from Microsoft-Windows-NTLM/Operational'`. 3 rules use the same requirement.

## Fields

The rules of this log source use the following field names:

- `EventID`
- `TargetName`
- `WorkstationName`
