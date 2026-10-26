---
id: "37226752754967"
titulo: "E0604 Rejeição: Não é permitido informar alíquota quando o prestador de serviço possui algum regime especial de tributação."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37226752754967-E0604-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-permitido-informar-al%C3%ADquota-quando-o-prestador-de-servi%C3%A7o-possui-algum-regime-especial-de-tributa%C3%A7%C3%A3o"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-10-07T12:34:56Z"
rotulos: ["Configuração", "Alíquota de ISS", "SEFAZ", "Impostos", "NFS-e", "Erro", "Artigo atualizado KCS", "Regime especial de tributação de ISS e a alíquota de ISS", "Não é permitido informar alíquota", "Regime esp. tributação ISS (NFS-e)", "Regime especial de tributação", "Docs Eletrônicos - KCS"]
---

# E0604 Rejeição: Não é permitido informar alíquota quando o prestador de serviço possui algum regime especial de tributação.

**MENSAGEM**

Regime esp. tributação ISS (NFS-e) não informado, opção de regime não aceita pela prefeitura ou rejeição E0604 (Rejeição: Não é permitido informar alíquota quando o prestador de serviço possui algum regime especial de tributação).

**SITUAÇÃO**

Esta mensagem é apresentada ao tentar emitir uma NFS-e quando o campo **"Regime esp. tributação ISS (NFS-e)"** não está preenchido, ou quando ocorre a rejeição E0604 por conflito entre o regime especial informado e o envio de alíquota de ISS.

**SOLUÇÃO**

Para resolver estes erros, ajuste as configurações seguindo os passos abaixo:

**(1)** Acesse a tela **"Empresa"** (Comercial >> Preferências >> Empresa) e localize a empresa emitente.

**(2)** Navegue até a aba **"Documentos Fiscais Eletrônicos"**, acesse a sub-aba **"NFS-e"** e a seção **"Geral"** (caso a aba não esteja visível, adicione-a como visível na grade de visualização).

**(3)** Localize o campo **"Regime esp. tributação ISS (NFS-e)"** e preencha com a opção adequada à situação tributária da empresa. Consulte a contabilidade para identificar a informação correta.

**Ajustes específicos para a rejeição E0604:**

- **Se a empresa possui regime especial:** Na tela "Empresa", aba "Documentos Fiscais Eletrônicos" >> "NFS-e", verifique o campo **"Enviar o Valor do ISS e alíquota no XML, apenas quando o ISS for devido a outro município?"**. Marcado, ele faz o sistema deixar de enviar a alíquota e o valor do ISS quando o imposto é devido no próprio município do prestador.
- **Se a empresa não possui regime especial:** altere o campo "Regime esp. tributação ISS (NFS-e)" para **"0 - Normal / Nenhum"**, salve e emita novamente.

**(5)** Salve as alterações e emita novamente a NFS-e. O documento deverá ser processado.

**Observações importantes:**

- Para algumas prefeituras, como a de **São Paulo**, o campo deve ser preenchido com a opção **"0 - Normal / Nenhum"**.
- Se depois de preencher o regime aparecer um erro relacionado ao CNAE, verifique se o campo "Cod. Trib. Município" está preenchido corretamente na aba "Alíquota ISS" do cadastro de "Serviço" (Configurações >> Cadastros >> Produtos >> Serviço).

**CAUSA**

O campo "Regime esp. tributação ISS (NFS-e)" é obrigatório para a maioria das prefeituras e precisa ter uma opção aceita pelo município. Já a rejeição E0604 vem da prefeitura ou do ambiente nacional da NFS-e: quando o prestador informa um regime especial de tributação, a legislação municipal não permite enviar a alíquota de ISS no documento.
