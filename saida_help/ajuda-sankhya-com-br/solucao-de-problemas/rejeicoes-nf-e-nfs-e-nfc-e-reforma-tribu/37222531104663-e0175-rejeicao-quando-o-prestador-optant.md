---
id: "37222531104663"
titulo: "E0175 Rejeição: Quando o prestador optante pelo Simples Nacional"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37222531104663-E0175-Rejei%C3%A7%C3%A3o-Quando-o-prestador-optante-pelo-Simples-Nacional"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-08-13T13:21:32Z"
rotulos: ["Configuração", "Simples Nacional", "SEFAZ", "Impostos", "NFS-e", "ISSQN", "Passos para resolver", "Erro", "Como Resolver", "Artigo atualizado KCS", "Regime tributário da empresa", "Empresa optante pelo Simples Nacional", "Regime de apuração", "Regime especial de tributação do ISSQN", "Fiscal/Contábil - KCS"]
---

# E0175 Rejeição: Quando o prestador optante pelo Simples Nacional

**Mensagem**

E0175 Rejeição: Quando o prestador optante pelo Simples Nacional tiver o regime de apuração dos tributos ocorrendo também pelo Simples Nacional, o regime especial de tributação do ISSQN deve ser "Nenhum" (regEspTrib = 0).

**Situação**

A **NFS-e** foi emitida por **empresa optante pelo Simples Nacional** com o regime de apuração configurado como Simples Nacional, porém com regime especial de tributação do ISSQN informado no documento fiscal.

**Solução**

Para corrigir este problema, siga os passos abaixo:

**(1)**Acesse a tela **"Empresas"** (Configurações >> Cadastros >> Empresas), localize a empresa emissora e, na aba **"Naturezas"**, verifique se o campo **"Cód. Regime Tribut."** está como **"Simples Nacional"** ou **"Simples Nacional - Sublimite"**.

**(2)** Acesse a tela **"Preferências da Empresa"** (Comercial >> Preferências >> Empresa). 
Localize a aba **"Documentos Fiscais Eletrônicos"** e acesse a sub-aba correspondente ao tipo de documento (NF-e ou NFS-e).

**(3)**  Acesse a sub-aba **"Geral"** e verifique se o campo **"Regime de Apuração dos Tributos do Simples Nacional"** está configurado como **"1 - Reg. Apuração Trib. Fed. e Mun. pelo SN"**.

**(4)** Identifique o campo **"Regime esp. tributação ISS (NFS-e)"**. Se a empresa for Simples Nacional com apuração pelo SN, altere este campo para **"Nenhum"** (valor 0).

**(5)** Salve as alterações clicando em **"Confirmar"** ou **"Salvar"**.

**(6)** Retorne à tela de emissão e tente emitir a nota novamente.

**Observações importantes:**

- **Consulte seu contador:** em caso de dúvida sobre o regime de tributação, consulte o responsável fiscal da empresa.
- **Classificação Tributária:** verifique também o campo **"Classificação Tributária"** (CLASSTRIB) no cadastro da empresa.

**Causa**

O erro ocorre devido à inconsistência de dados entre o cadastro no sistema e o portal da prefeitura ou Sefaz. Especificamente para o Simples Nacional, a rejeição ocorre pois não é permitido informar um regime especial de tributação do ISSQN diferente de "Nenhum" para empresas com regime de apuração configurado como Simples Nacional, visando evitar divergências fiscais.
