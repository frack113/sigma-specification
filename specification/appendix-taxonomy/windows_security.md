# product: windows, service: security

```yaml
logsource:
    product: windows
    service: security
```

<!-- mdformat-toc start --slug=github --no-anchors --maxlevel=6 --minlevel=2 -->

- [Description](#description)
- [Telemetry](#telemetry)
- [Points of Attention](#points-of-attention)
- [Fields](#fields)

<!-- mdformat-toc end -->

## Description

The events of the security channel of a Windows host, that is the audit events of the security subsystem. The events are grouped in the audit policies of the Advanced Audit Policy Configuration, they are listed in the `## Telemetry` section.

## Telemetry

Events read from the `Security` channel, written by the `Microsoft Windows Security Auditing` provider.

| Audit Policy       | Subcategory                            | GUID                                   | EventIDs                                                                                                                                                                                                                                       |
| ------------------ | -------------------------------------- | -------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Account Logon      | Credential Validation                  | `0CCE923F-69AE-11D9-BED3-505054503030` | 4774, 4775, 4776, 4777                                                                                                                                                                                                                         |
| Account Logon      | Kerberos Authentication Service        | `0CCE9242-69AE-11D9-BED3-505054503030` | 4768, 4771, 4772                                                                                                                                                                                                                               |
| Account Logon      | Kerberos Service Ticket Operations     | `0CCE9240-69AE-11D9-BED3-505054503030` | 4769, 4770, 4773                                                                                                                                                                                                                               |
| Account Logon      | Other Account Logon Events             | `0CCE9241-69AE-11D9-BED3-505054503030` | TBD                                                                                                                                                                                                                                            |
| Account Management | Application Group Management           | `0CCE9239-69AE-11D9-BED3-505054503030` | 4783, 4784, 4785, 4786, 4787, 4788, 4789, 4790, 4791, 4792                                                                                                                                                                                     |
| Account Management | Computer Account Management            | `0CCE9236-69AE-11D9-BED3-505054503030` | 4741, 4742, 4743                                                                                                                                                                                                                               |
| Account Management | Distribution Group Management          | `0CCE9238-69AE-11D9-BED3-505054503030` | 4749, 4750, 4751, 4752, 4753                                                                                                                                                                                                                   |
| Account Management | Other Account Management Events        | `0CCE923A-69AE-11D9-BED3-505054503030` | 4782, 4793                                                                                                                                                                                                                                     |
| Account Management | Security Group Management              | `0CCE9237-69AE-11D9-BED3-505054503030` | 4728, 4731, 4732, 4733, 4734, 4735, 4764, 4799, 4727, 4737, 4729, 4730, 4754, 4755, 4756, 4757, 4758                                                                                                                                           |
| Account Management | User Account Management                | `0CCE9235-69AE-11D9-BED3-505054503030` | 4720, 4722, 4723, 4724, 4725, 4726, 4738, 4740, 4765, 4766, 4767, 4780, 4781, 4794, 4798, 5376, 5377                                                                                                                                           |
| Detailed Tracking  | DPAPI Activity                         | `0CCE922D-69AE-11D9-BED3-505054503030` | 4692, 4693, 4694, 4695                                                                                                                                                                                                                         |
| Detailed Tracking  | PNP Activity                           | `0CCE9248-69AE-11D9-BED3-505054503030` | 6416, 6419, 6420, 6421, 6422, 6423, 6424                                                                                                                                                                                                       |
| Detailed Tracking  | Process Creation                       | `0CCE922B-69AE-11D9-BED3-505054503030` | 4688, 4696                                                                                                                                                                                                                                     |
| Detailed Tracking  | Process Termination                    | `0CCE922C-69AE-11D9-BED3-505054503030` | 4689                                                                                                                                                                                                                                           |
| Detailed Tracking  | RPC Events                             | `0CCE922E-69AE-11D9-BED3-505054503030` | 5712                                                                                                                                                                                                                                           |
| Detailed Tracking  | Token Right Adjusted                   | `0CCE924A-69AE-11D9-BED3-505054503030` | 4703                                                                                                                                                                                                                                           |
| DS Access          | Detailed Directory Service Replication | `0CCE923E-69AE-11D9-BED3-505054503030` | 4928, 4929, 4930, 4931, 4934, 4935, 4936, 4937                                                                                                                                                                                                 |
| DS Access          | Directory Service Access               | `0CCE923B-69AE-11D9-BED3-505054503030` | 4661, 4662                                                                                                                                                                                                                                     |
| DS Access          | Directory Service Changes              | `0CCE923C-69AE-11D9-BED3-505054503030` | 5136, 5137, 5138, 5139, 5141                                                                                                                                                                                                                   |
| DS Access          | Directory Service Replication          | `0CCE923D-69AE-11D9-BED3-505054503030` | 4932, 4933                                                                                                                                                                                                                                     |
| Logon/Logoff       | Account Lockout                        | `0CCE9217-69AE-11D9-BED3-505054503030` | 4625                                                                                                                                                                                                                                           |
| Logon/Logoff       | User/Device Claims                     | `0CCE9247-69AE-11D9-BED3-505054503030` | 4626                                                                                                                                                                                                                                           |
| Logon/Logoff       | Group Membership                       | `0CCE9249-69AE-11D9-BED3-505054503030` | 4627                                                                                                                                                                                                                                           |
| Logon/Logoff       | IPsec Extended Mode                    | `0CCE921A-69AE-11D9-BED3-505054503030` | 4978, 4979, 4980, 4981, 4982, 4983, 4984                                                                                                                                                                                                       |
| Logon/Logoff       | IPsec Main Mode                        | `0CCE9218-69AE-11D9-BED3-505054503030` | 4646, 4650, 4651, 4652, 4653, 4655, 4976, 5049, 5453                                                                                                                                                                                           |
| Logon/Logoff       | IPsec Quick Mode                       | `0CCE9219-69AE-11D9-BED3-505054503030` | 4977, 5451, 5452                                                                                                                                                                                                                               |
| Logon/Logoff       | Logoff                                 | `0CCE9216-69AE-11D9-BED3-505054503030` | 4634, 4647                                                                                                                                                                                                                                     |
| Logon/Logoff       | Logon                                  | `0CCE9215-69AE-11D9-BED3-505054503030` | 4624, 4625, 4648, 4675                                                                                                                                                                                                                         |
| Logon/Logoff       | Network Policy Server                  | `0CCE9243-69AE-11D9-BED3-505054503030` | 6272, 6273, 6274, 6275, 6276, 6277, 6278, 6279, 6280                                                                                                                                                                                           |
| Logon/Logoff       | Other Logon/Logoff Events              | `0CCE921C-69AE-11D9-BED3-505054503030` | 4649, 4778, 4779, 4800, 4801, 4802, 4803, 5378, 5632, 5633                                                                                                                                                                                     |
| Logon/Logoff       | Special Logon                          | `0CCE921B-69AE-11D9-BED3-505054503030` | 4964, 4672                                                                                                                                                                                                                                     |
| Object Access      | Application Generated                  | `0CCE9222-69AE-11D9-BED3-505054503030` | 4665, 4666, 4667, 4668                                                                                                                                                                                                                         |
| Object Access      | Certification Services                 | `0CCE9221-69AE-11D9-BED3-505054503030` | 4868, 4869, 4870, 4871, 4872, 4873, 4874, 4875, 4876, 4877, 4878, 4879, 4880, 4881, 4882, 4883, 4884, 4885, 4886, 4887, 4888, 4889, 4890, 4891, 4892, 4893, 4894, 4895, 4896, 4897, 4898                                                       |
| Object Access      | Detailed File Share                    | `0CCE9244-69AE-11D9-BED3-505054503030` | 5145                                                                                                                                                                                                                                           |
| Object Access      | File Share                             | `0CCE9224-69AE-11D9-BED3-505054503030` | 5140, 5142, 5143, 5144, 5168                                                                                                                                                                                                                   |
| Object Access      | File System                            | `0CCE921D-69AE-11D9-BED3-505054503030` | 4656, 4658, 4660, 4663, 4664, 4670, 4985, 5051                                                                                                                                                                                                 |
| Object Access      | Filtering Platform Connection          | `0CCE9226-69AE-11D9-BED3-505054503030` | 5031, 5150, 5151, 5154, 5155, 5156, 5157, 5158, 5159                                                                                                                                                                                           |
| Object Access      | Filtering Platform Packet Drop         | `0CCE9225-69AE-11D9-BED3-505054503030` | 5152, 5153                                                                                                                                                                                                                                     |
| Object Access      | Handle Manipulation                    | `0CCE9223-69AE-11D9-BED3-505054503030` | 4658, 4690                                                                                                                                                                                                                                     |
| Object Access      | Kernel Object                          | `0CCE921F-69AE-11D9-BED3-505054503030` | 4656, 4658, 4660, 4663                                                                                                                                                                                                                         |
| Object Access      | Other Object Access Events             | `0CCE9227-69AE-11D9-BED3-505054503030` | 4671, 4691, 4698, 4699, 4700, 4701, 4702, 5148, 5149, 5888, 5889, 5890                                                                                                                                                                         |
| Object Access      | Registry                               | `0CCE921E-69AE-11D9-BED3-505054503030` | 4656, 4657, 4658, 4660, 4663, 4670, 5039                                                                                                                                                                                                       |
| Object Access      | Removable Storage                      | `0CCE9245-69AE-11D9-BED3-505054503030` | 4656, 4658, 4663                                                                                                                                                                                                                               |
| Object Access      | SAM                                    | `0CCE9220-69AE-11D9-BED3-505054503030` | 4661                                                                                                                                                                                                                                           |
| Object Access      | Central Access Policy Staging          | `0CCE9246-69AE-11D9-BED3-505054503030` | 4818                                                                                                                                                                                                                                           |
| Policy Change      | Audit Policy Change                    | `0CCE922F-69AE-11D9-BED3-505054503030` | 4715, 4719, 4817, 4902, 4906, 4907, 4908, 4912, 4904, 4905                                                                                                                                                                                     |
| Policy Change      | Authentication Policy Change           | `0CCE9230-69AE-11D9-BED3-505054503030` | 4670, 4706, 4707, 4716, 4713, 4717, 4718, 4739, 4864, 4865, 4866, 4867                                                                                                                                                                         |
| Policy Change      | Authorization Policy Change            | `0CCE9231-69AE-11D9-BED3-505054503030` | 4703, 4704, 4705, 4670, 4911, 4913                                                                                                                                                                                                             |
| Policy Change      | Filtering Platform Policy Change       | `0CCE9233-69AE-11D9-BED3-505054503030` | 4709, 4710, 4711, 4712, 5040, 5041, 5042, 5043, 5044, 5045, 5046, 5047, 5048, 5440, 5441, 5442, 5443, 5444, 5446, 5448, 5449, 5450, 5456, 5457, 5458, 5459, 5460, 5461, 5462, 5463, 5464, 5465, 5466, 5467, 5468, 5471, 5472, 5473, 5474, 5477 |
| Policy Change      | MPSSVC Rule-Level Policy Change        | `0CCE9232-69AE-11D9-BED3-505054503030` | 4944, 4945, 4946, 4947, 4948, 4949, 4950, 4951, 4952, 4953, 4954, 4956, 4957, 4958                                                                                                                                                             |
| Policy Change      | Other Policy Change Events             | `0CCE9234-69AE-11D9-BED3-505054503030` | 4714, 4819, 4826, 4909, 4910, 5063, 5064, 5065, 5066, 5067, 5068, 5069, 5070, 5447, 6144, 6145                                                                                                                                                 |
| Privilege Use      | Non Sensitive Privilege Use            | `0CCE9229-69AE-11D9-BED3-505054503030` | 4673, 4674, 4985                                                                                                                                                                                                                               |
| Privilege Use      | Other Privilege Use Events             | `0CCE922A-69AE-11D9-BED3-505054503030` | 4985                                                                                                                                                                                                                                           |
| Privilege Use      | Sensitive Privilege Use                | `0CCE9228-69AE-11D9-BED3-505054503030` | TBD                                                                                                                                                                                                                                            |
| System             | IPsec Driver                           | `0CCE9213-69AE-11D9-BED3-505054503030` | 4960, 4961, 4962, 4963, 4965, 5478, 5479, 5480, 5483, 5484, 5485                                                                                                                                                                               |
| System             | Other System Events                    | `0CCE9214-69AE-11D9-BED3-505054503030` | 5024, 5025, 5027, 5028, 5029, 5030, 5032, 5033, 5034, 5035, 5037, 5058, 5059, 6400, 6401, 6402, 6403, 6404, 6405, 6406, 6407, 6408, 6409                                                                                                       |
| System             | Security State Change                  | `0CCE9210-69AE-11D9-BED3-505054503030` | 4608, 4616, 4621                                                                                                                                                                                                                               |
| System             | Security System Extension              | `0CCE9211-69AE-11D9-BED3-505054503030` | 4610, 4611, 4614, 4622, 4697                                                                                                                                                                                                                   |
| System             | System Integrity                       | `0CCE9212-69AE-11D9-BED3-505054503030` | 4612, 4615, 4618, 4816, 5038, 5056, 5062, 5057, 5060, 5061, 6281, 6410                                                                                                                                                                         |

## Points of Attention

This section summarizes the logsource guide [`documentation/logsource-guides/windows/service/security.md`](https://github.com/SigmaHQ/sigma/blob/master/documentation/logsource-guides/windows/service/security.md) of the rules repository, that describes each of the audit policies above with its own commands.

- No event is written by default. Every rule that matches on an event of this log source needs the audit policy that writes it to be enabled, the requirement is written in the `definition` of the rule, for example `Requirements: Audit Policy : Object Access > Audit Registry (Success)`.
- A subcategory is enabled with the Advanced Audit Policy Configuration of the `gpedit.msc` or with `auditpol`:

```powershell
# Enable Success audit Only
auditpol /set /subcategory:{0CCE9215-69AE-11D9-BED3-505054503030}, /success:enable

# Enable both Success and Failure auditing
auditpol /set /subcategory:{0CCE9215-69AE-11D9-BED3-505054503030}, /success:enable /failure:enable
```

- The events of the `Object Access` and of the `DS Access` policies are only written for the objects that have a system access control list (SACL) that audits the access, not only the audit policy has to be enabled. A rule that needs one of them declares it in its `definition`.
- The `Logon` events are high volume on a client computer and very high volume on a domain controller.
- The event identifiers of the subcategories that are marked `TBD` are not documented yet in the logsource guide, the page keeps the same value.

## Fields

The rules of this log source use the following field names:

- `AccessList`
- `AccessMask`
- `AdditionalInfo`
- `AllowedToDelegateTo`
- `Application`
- `AttributeLDAPDisplayName`
- `AttributeValue`
- `AuditPolicyChanges`
- `AuditSourceName`
- `AuthenticationPackageName`
- `CertThumbprint`
- `DestAddress`
- `DestPort`
- `EventID`
- `FilterName`
- `FilterOrigin`
- `ImpersonationLevel`
- `IpAddress`
- `IpPort`
- `KeyLength`
- `Keywords`
- `LayerRTID`
- `LogonProcessName`
- `LogonType`
- `NewTargetUserName`
- `NewTemplateContent`
- `NewUacValue`
- `NewValue`
- `ObjectClass`
- `ObjectDN`
- `ObjectName`
- `ObjectServer`
- `ObjectType`
- `ObjectValueName`
- `OldUacValue`
- `PreAuthType`
- `PrivilegeList`
- `ProcessName`
- `Properties`
- `ProviderContextName`
- `Provider_Name`
- `RelativeTargetName`
- `SamAccountName`
- `Service`
- `ServiceFileName`
- `ServiceName`
- `ServicePrincipalNames`
- `ServiceStartType`
- `ServiceType`
- `ShareName`
- `SidHistory`
- `SourceAddress`
- `SourcePort`
- `Status`
- `SubcategoryGuid`
- `SubjectDomainName`
- `SubjectLogonId`
- `SubjectUserName`
- `SubjectUserSid`
- `TargetName`
- `TargetOutboundUserName`
- `TargetServerName`
- `TargetUserName`
- `TargetUserSid`
- `TaskContent`
- `TaskContentNew`
- `TaskName`
- `TemplateContent`
- `TicketEncryptionType`
- `TicketOptions`
- `Workstation`
- `WorkstationName`
- `param1`
