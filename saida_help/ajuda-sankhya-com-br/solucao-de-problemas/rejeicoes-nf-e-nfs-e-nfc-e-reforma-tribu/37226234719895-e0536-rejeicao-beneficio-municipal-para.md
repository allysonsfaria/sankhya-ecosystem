---
id: "37226234719895"
titulo: "E0536 Rejeição: Benefício Municipal para ME/EPP no Simples Nacional"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37226234719895-E0536-Rejei%C3%A7%C3%A3o-Benef%C3%ADcio-Municipal-para-ME-EPP-no-Simples-Nacional"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:15:09Z"
rotulos: ["ISS", "Configuração", "Simples Nacional", "XML", "Prefeituras", "NFS-e", "Benefício Municipal", "ME/EPP", "Empresas ME/EPP optantes pelo Simples Nacional", "ME/EPP no Simples Nacional", "Microempresário e Empresa de Pequeno Porte (ME EPP)", "Benefício Municipal para ME/EPP"]
---

# E0536 Rejeição: Benefício Municipal para ME/EPP no Simples Nacional

**MENSAGEM:**

E0536 Rejeição: Benefício Municipal para ME/EPP no Simples Nacional

**SITUAÇÃO:**

Ao emitir uma NFS-e, o sistema retorna a rejeição **E0536** ao identificar o preenchimento de informações de benefício municipal no documento fiscal.

**SOLUÇÃO:**

**Passo 1: Configuração da Empresa**

**(1)** Acesse a tela **''Empresa''** (Comercial » Preferências » Empresa)

**(2)** Vá até a aba **NFS-e**.

**(3)** Localize o campo **"Cód. Reg. Esp. trib. ISS (NFS-e)"**.

**(4)** Confirme se está selecionado o código **6 - Microempresário e Empresa de Pequeno Porte (ME EPP)**.

**Passo 2: Revise a Configuração do Tipo de Operação (TOP)**

**(1)** Acesse a tela **''Tipo de Operações - TOP''** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP).

**(2)** Localize o TOP utilizado na emissão da nota

**(3)** Na aba **''NFS-e''**, verifique o campo **''Cód. Natureza Oper. ISS (NFS-e)"**.

**(4)** Certifique-se de que está configurado corretamente conforme a operação:

- **1 - Exigível**
- **2 - Não incidência**
- **3 - Isenção**
- **4 - Exportação**
- **5 - Imunidade**
- **6 - Exigibilidade suspensa por decisão judicial**
- **7 - Exigibilidade suspensa por procedimento administrativo**

**Passo 3: Remova as informações do Benefício Municipal**

Para empresas ME/EPP no Simples Nacional, não devem ser preenchidas informações relacionadas a benefícios fiscais municipais quando o código de serviço do município não permitir.

Verifique:

- Se há campos de benefício fiscal preenchidos nas configurações da empresa;
- Se há informações de incentivo fiscal configuradas no cadastro de serviços;
- Remova quaisquer referências a benefícios municipais que estejam sendo enviadas no XML.

**Passo 4: Valide o Código de Serviço**

**(1)** Consulte junto à prefeitura do município de incidência do ISSQN se o código de serviço utilizado permite benefícios fiscais para ME/EPP no Simples Nacional.

**(2)** Caso necessário, utilize um código de serviço diferente que seja compatível com a situação tributária da empresa.

**Passo 5: Reemita a NFS-e**

**(1)** Após realizar os ajustes, tente emitir novamente a NFS-e.

**(2)** Verifique se a rejeição foi solucionada.

**OBSERVAÇÕES**:

A parametrização de códigos de serviço e benefícios fiscais varia de município para município. Empresas ME/EPP optantes pelo Simples Nacional possuem tratamento tributário específico que pode limitar o uso de determinados benefícios municipais.

Sempre consulte a legislação municipal específica para entender as regras aplicáveis ao seu caso. Se após seguir todos os passos a rejeição persistir, revise novamente todas as configurações relacionadas ao regime tributário da empresa e à natureza da operação utilizada.

**CAUSA:**

Esta rejeição acontece porque a empresa está configurada como ME/EPP optante pelo Simples Nacional. O município de incidência do ISSQN possui parametrização específica para o código de serviço que não permite o preenchimento de benefícios municipais para empresas nesta condição tributária. Há informações de benefício fiscal municipal sendo enviadas no XML da NFS-e .
