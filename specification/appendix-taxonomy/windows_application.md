# product: windows, service: application

```yaml
logsource:
    product: windows
    service: application
```

<!-- mdformat-toc start --slug=github --no-anchors --maxlevel=6 --minlevel=2 -->

- [Telemetry](#telemetry)
- [Points of Attention](#points-of-attention)
- [Fields](#fields)

<!-- mdformat-toc end -->

## Telemetry

- Channel: Application

## Points of Attention

- 4 different requirements are declared in the `definition` of the rules of this log source, they are written rule by rule.

## Fields

The rules of this log source use the following field names:

- `AppName`
- `Data`
- `EventID`
- `ExceptionCode`
- `Level`
- `Message`
- `Provider_Name`
