# 论文GitHub发布方案 Spec

## Why
用户希望将学术论文《类脑AGI架构"天元"系统》正式发布到GitHub平台，要求明确禁止商用，当前README.md中使用的是CC-BY 4.0协议（允许商用），需要调整为禁止商用的许可协议，并完善仓库结构以满足学术发布的规范要求。

## What Changes
- **BREAKING** 将LICENSE从CC-BY 4.0更改为CC-BY-NC 4.0（禁止商用）
- 更新README.md中的版权说明部分，删除或修改商用相关条款
- 创建标准的GitHub仓库结构（paper/、data/、code/目录）
- 添加.gitignore文件以排除不必要的文件
- 创建LICENSE文件明确禁止商用
- 优化README.md的格式和内容结构

## Impact
- Affected specs: 版权许可协议、仓库目录结构、README文档
- Affected code: README.md、LICENSE、.gitignore、目录结构

## ADDED Requirements

### Requirement: 禁止商用的许可协议
系统 SHALL 使用CC-BY-NC 4.0协议，明确禁止商业使用，同时保留署名要求。

#### Scenario: 用户访问仓库
- **WHEN** 用户访问GitHub仓库
- **THEN** 能在根目录看到LICENSE文件，明确标注CC-BY-NC 4.0协议
- **AND** README.md中清晰说明禁止商用的条款

### Requirement: 标准学术仓库结构
系统 SHALL 提供标准的学术论文仓库目录结构，便于读者理解和使用。

#### Scenario: 读者浏览仓库
- **WHEN** 读者克隆或浏览仓库
- **THEN** 能看到清晰的目录结构：paper/（论文文件）、data/（实验数据）、code/（代码）
- **AND** 每个目录下有README说明文件

### Requirement: 完整的版权声明
系统 SHALL 在README.md中提供完整的版权声明，明确禁止商用，保留作者权益。

#### Scenario: 第三方使用论文
- **WHEN** 第三方想要使用论文内容
- **THEN** 能从README.md中清楚了解使用限制（禁止商用、必须署名）
- **AND** 知道如何联系作者获取授权

## MODIFIED Requirements

### Requirement: README.md版权说明部分
原README.md中的"版权购买与变现说明"部分需要大幅修改：
- 删除"场景1：遵循当前CC-BY 4.0协议变现（无需单独授权）"相关内容
- 明确标注"本论文禁止商用"
- 简化版权说明，突出禁止商用和署名要求
- 保留联系方式

## REMOVED Requirements

### Requirement: CC-BY 4.0协议
**Reason**: 该协议允许商用，不符合用户"禁止商用"的要求
**Migration**: 更改为CC-BY-NC 4.0协议，保留署名要求，增加非商业使用限制
