---
id: "37227168610839"
titulo: "E0684 Rejeição: A alíquota do PIS deve ser informada quando a base de cálculo deste imposto for informada."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37227168610839-E0684-Rejei%C3%A7%C3%A3o-A-al%C3%ADquota-do-PIS-deve-ser-informada-quando-a-base-de-c%C3%A1lculo-deste-imposto-for-informada"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:14:29Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "Alíquotas de PIS", "Código de Situação Tributária - CST", "Alíquota do PIS não foi informada", "Alíquota correspondente não foi preenchida", "Alíquota do PIS", "Base de cálculo do PIS"]
---

# E0684 Rejeição: A alíquota do PIS deve ser informada quando a base de cálculo deste imposto for informada.

**MENSAGEM**

E0684 Rejeição: A alíquota do PIS deve ser informada quando a base de cálculo deste imposto for informada.

**SITUAÇÃO**

Ao emitir uma NF-e ou NFC-e, o sistema calculou a **base de cálculo do PIS** para um ou mais itens do documento fiscal, porém a **alíquota do PIS não foi informada** no cadastro de alíquotas. Como resultado, a nota foi rejeitada pela Sefaz com a mensagem E0684, indicando que é obrigatório informar a alíquota quando há base de cálculo do imposto.

**SOLUÇÃO**

Para resolver esta rejeição, configure corretamente a alíquota de PIS no cadastro de alíquotas:

**(1)** Acesse a tela **"Alíquota de PIS"** (Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de PIS).

**(2)** Localize o registro de alíquota correspondente ao **produto** e ao **"Código de situação tributária - CST"** utilizado na nota fiscal rejeitada.

**(3)** Verifique se o campo **"Alíquota"** está preenchido com o percentual correto do PIS:

- Se o campo estiver **vazio ou zerado**, informe a alíquota adequada conforme a legislação vigente e o regime tributário da empresa.
- Certifique-se de que o campo **"Tipo"** da alíquota está configurado corretamente como **"Entrada"** ou **"Saída"**, de acordo com o CST informado.

**(4)** Confirme que a marcação **"Produto sem tributação"** não está ativada, pois ela zera automaticamente os campos de alíquota.

**(5)** Salve as alterações realizadas no cadastro de alíquotas.

**(6)** Retorne ao documento fiscal rejeitado e realize uma nova tentativa de transmissão da nota. 

**CAUSA**

A rejeição ocorreu porque o sistema identificou que existe uma **base de cálculo do PIS** informada no documento fiscal, mas a **alíquota correspondente não foi preenchida** no cadastro de **"Alíquota de PIS"**. Segundo a legislação tributária e as regras de validação da Sefaz, sempre que houver base de cálculo para o imposto, é obrigatório informar a alíquota aplicável. A ausência dessa informação impede a correta apuração do tributo e, consequentemente, a autorização do documento fiscal.
