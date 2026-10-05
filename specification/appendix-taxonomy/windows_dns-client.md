# product: windows, service: dns-client

```yaml
logsource:
    product: windows
    service: dns-client
```

<!-- mdformat-toc start --slug=github --no-anchors --maxlevel=6 --minlevel=2 -->

- [Telemetry](#telemetry)
- [Points of Attention](#points-of-attention)
- [Fields](#fields)

<!-- mdformat-toc end -->

## Telemetry

- Channel: Microsoft-Windows-DNS Client Events/Operational

## Points of Attention

- The rules set `definition: 'Requirements: Microsoft-Windows-DNS Client Events/Operational Event Log must be enabled/collected in order to receive the events.'`. 6 rules use the same requirement.

## Fields

The rules of this log source use the following field names:

- `EventID`
- `QueryName`
