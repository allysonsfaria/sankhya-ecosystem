---
id: "37227188958871"
titulo: "E0686 Rejeição: A alíquota do PIS deve ser igual ou maior que 0 e menor ou igual a 100%."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37227188958871-E0686-Rejei%C3%A7%C3%A3o-A-al%C3%ADquota-do-PIS-deve-ser-igual-ou-maior-que-0-e-menor-ou-igual-a-100"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:14:27Z"
rotulos: ["Produtos", "Configuração", "NF-e", "SEFAZ", "Impostos", "TOP", "Alíquota do PIS", "Alíquota fora do intervalo permitido", "Alíquota de PIS inválida", "Grupo PIS", "Cálculo do PIS"]
---

# E0686 Rejeição: A alíquota do PIS deve ser igual ou maior que 0 e menor ou igual a 100%.

**MENSAGEM**

E0686 Rejeição: A alíquota do PIS deve ser igual ou maior que 0 e menor ou igual a 100%.

**SITUAÇÃO**

Ao emitir um documento fiscal (NF-e ou NFC-e), o sistema **rejeitou a nota** informando que a alíquota de PIS configurada está **fora do intervalo permitido**.

**SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **"Produtos"** (Configurações » Cadastros » Produtos » Produtos) e identifique o produto utilizado no documento fiscal rejeitado.

**(2)** Na aba **"Impostos"**, verifique o valor informado no campo **"Grupo PIS"**.

**(3)** Acesse a tela **"Alíquotas de PIS"** (Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de PIS).

**(4)** Localize o cadastro de alíquota correspondente ao **"Grupo PIS"** identificado no passo 2, filtrando por:

- Empresa
- TOP (Tipo de Operação)
- Parceiro
- Tipo (Saída/Entrada)

**(5)** Verifique o valor informado no campo **"Alíquota''** e certifique-se de que está **entre 0% e 100%**.

**(6)** Caso o valor esteja **fora do intervalo permitido**, ajuste a alíquota para um valor válido (entre 0 e 100).

**(7)** Consulte o **contador responsável** para confirmar a alíquota correta de PIS e o **"Código de situação tributária - CST"** adequado para a operação.

**(8)** Após realizar os ajustes necessários, **fature novamente** o documento fiscal ou **redigite o item** na nota e gere um novo lote para transmissão.

**OBSERVAÇÕES:**

- O **cálculo de PIS e COFINS é obrigatório** para todas as movimentações de venda, mesmo que a incidência seja zero.
- Recomenda-se sempre **criar regras específicas** para o respectivo tipo de movimento.
- Revise também as marcações de PIS no cadastro da **"Empresa"** (Comercial » Preferências » Empresa) e no **"TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP).

**CAUSA**

A rejeição ocorre porque foi informada uma **alíquota de PIS inválida** no cadastro de **"Alíquotas de PIS"**, com valor **menor que 0% ou maior que 100%**. A Sefaz valida que todas as alíquotas de impostos devem estar dentro do intervalo permitido (entre 0 e 100), e qualquer valor fora deste range resulta na rejeição do documento fiscal.
