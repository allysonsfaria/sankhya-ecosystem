---
id: "37098705859095"
titulo: "1034 Rejeição: Percentual de redução de alíquota da UF não é válido para este cClassTrib [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37098705859095-1034-Rejei%C3%A7%C3%A3o-Percentual-de-redu%C3%A7%C3%A3o-de-al%C3%ADquota-da-UF-n%C3%A3o-%C3%A9-v%C3%A1lido-para-este-cClassTrib-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:20:11Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "Código de Situação Tributária", "Lei Complementar 214/2025", "Alíquotas de CBS", "Alíquotas de IBS", "Classificação tributária do contribuinte na nota fiscal", "cClassTrib", "Percentual de redução de alíquota", "Redução de alíquota do IBS", "1034 Rejeição", "Rejeição 1034"]
---

# 1034 Rejeição: Percentual de redução de alíquota da UF não é válido para este cClassTrib [nItem: 999]

**MENSAGEM**

1034 Rejeição: Percentual de redução de alíquota da UF não é válido para este cClassTrib [nItem: 999]

**SITUAÇÃO**

Ao emitir o documento fiscal, o sistema retorna uma rejeição relacionada ao percentual de redução de alíquota do IBS informado em conjunto com a classificação tributária do contribuinte na nota fiscal.

**SOLUÇÃO**

**(1)** Acesse a tela [**''Portal de Vendas''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas) (Comercial » Consultas » Portal de Vendas).

**(2)** Localize a ''**NF-e''** que apresentou a rejeição.

(Ao selecionar o documento, a Central de Vendas será aberta automaticamente) 

**(3)**  Na [''**Central de Vendas''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas) (Comercial » Rotinas),  **selecione o item** que recebeu a rejeição. Depois clique no botão **''Outras Opções do Item''** (ícone de três pontos). Em seguida, selecione a opção **''Consultar/Alterar Dados do Imposto do Item''** e identifique o código da alíquota utilizada.

**(4)** Acesse a tela **"Alíquotas IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e/ou **''Alíquota de CBS"** (Livros Fiscais » Cadastros » Aliquotas de CBS). Pesquise e selecione a alíquota identificada no passo 3.

**(5)** Na alíquota, verifique o **CST e a Classificação Tributária (cClassTrib) do IBS/CBS** que está sendo utilizado na operação. **É importante que eles sejam correspondentes.** Caso não sejam, faça as devidas correções.

- **Observação:** para verificar a Classificação Tributária (cClassTrib) correspondente para cada CST, consulte a tabela: [**Classificação Tributária**](https://dfe-portal.svrs.rs.gov.br/Cff/ClassificacaoTributaria)

**(6)** Um vez informado o CST e a Classificação Tributária (cClassTrib) corretos, preencha o campo **"% da Redução de Alíquota IBS/CBS Estadual"** com a porcentagem correspondente à Classificação Tributária que está sendo utilizada.

- Novamente, para saber o percentual correto de redução, confira a tabela: [**Classificação Tributária**](https://dfe-portal.svrs.rs.gov.br/Cff/ClassificacaoTributaria)

**(7)** Após realizar os ajustes necessários, tente emitir a nota fiscal novamente.

**CAUSA**

A rejeição ocorre porque a Sefaz implementou uma validação que verifica a compatibilidade entre o percentual de redução de alíquota do IBS/CBS informado e a classificação tributária do contribuinte (cClassTrib). Cada classificação tributária possui regras específicas sobre quais percentuais de redução podem ser aplicados, conforme estabelecido na Lei Complementar 214/2025 que regulamenta a Reforma Tributária.

Quando o sistema identifica um percentual de redução que não está previsto para determinada classificação tributária, a nota fiscal é rejeitada com o código 1034, indicando que o percentual informado não é válido para o cClassTrib do contribuinte. Esta validação faz parte das novas regras implementadas com a Reforma Tributária, que visa padronizar e controlar a aplicação de benefícios fiscais relacionados ao IBS.
