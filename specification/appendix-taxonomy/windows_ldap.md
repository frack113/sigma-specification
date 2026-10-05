# product: windows, service: ldap

```yaml
logsource:
    product: windows
    service: ldap
```

<!-- mdformat-toc start --slug=github --no-anchors --maxlevel=6 --minlevel=2 -->

- [Telemetry](#telemetry)
- [Points of Attention](#points-of-attention)
- [Fields](#fields)

<!-- mdformat-toc end -->

## Telemetry

- Channel: Microsoft-Windows-LDAP-Client/Debug

## Points of Attention

- The rules set `definition: 'Requirements: Microsoft-Windows-LDAP-Client/Debug ETW logging'`.

## Fields

The rules of this log source use the following field names:

- `DistinguishedName`
- `EventID`
- `SearchFilter`
