---
id: "37226433778967"
titulo: "E0579 Rejeição: É obrigatório informar pRedBCBM quando o código de identificação do Benefício Municipal (nBM) for um benefício do tipo Redução de Base de Cálculo por percentual."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37226433778967-E0579-Rejei%C3%A7%C3%A3o-%C3%89-obrigat%C3%B3rio-informar-pRedBCBM-quando-o-c%C3%B3digo-de-identifica%C3%A7%C3%A3o-do-Benef%C3%ADcio-Municipal-nBM-for-um-benef%C3%ADcio-do-tipo-Redu%C3%A7%C3%A3o-de-Base-de-C%C3%A1lculo-por-percentual"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:14:57Z"
rotulos: ["Configuração", "NF-e", "Alíquota de ISS", "SEFAZ", "Impostos", "NFS-e", "Código de benefício municipal", "Código de Classificação Tributária", "percentual de redução", "Redução de Base de Cálculo por percentual", "Redução percentual da base de cálculo do ISS Municipal"]
---

# E0579 Rejeição: É obrigatório informar pRedBCBM quando o código de identificação do Benefício Municipal (nBM) for um benefício do tipo Redução de Base de Cálculo por percentual.

**MENSAGEM**

E0579 Rejeição: É obrigatório informar pRedBCBM quando o código de identificação do Benefício Municipal (nBM) for um benefício do tipo Redução de Base de Cálculo por percentual.

**SITUAÇÃO**

O documento fiscal eletrônico (NF-e ou NFC-e) foi emitido com a informação de código de benefício municipal que indica redução percentual da base de cálculo do ISS Municipal, sem o preenchimento do percentual de redução correspondente no documento.

**SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

**(1)** Acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS) e verifique a alíquota utilizada no documento fiscal rejeitado.

**(2)** Na aba **''Tributação''**, verifique se o campo **''Código de Classificação Tributária''** está preenchido com um código que representa benefício do tipo **Redução de Base de Cálculo por percentual**.

**(3)** Certifique-se de que o campo **''% da Redução de Alíquota IBS Municipal''** esteje preenchido com o percentual correto da redução da base de cálculo, conforme estabelecido pela legislação municipal.

**(4)** Caso não saiba qual percentual informar, consulte seu contador ou a legislação tributária municipal para obter o **percentual de redução correto** aplicável ao benefício fiscal cadastrado.

**(5)** Salve as alterações.

**(6)** Retorne ao documento fiscal rejeitado, exclua os itens e insira-os novamente para que as informações atualizadas da alíquota sejam carregadas corretamente.

**(7)** Transmita novamente o documento fiscal para a Sefaz.

**CAUSA**

A rejeição ocorre porque a **legislação fiscal exige** que, quando um benefício municipal do tipo **"Redução de Base de Cálculo por percentual"** é informado no documento fiscal através do código de identificação do benefício (nBM), o **percentual de redução correspondente (pRedBCBM)** seja obrigatoriamente declarado. A ausência desta informação impede a validação correta do documento pela Sefaz, pois não é possível calcular adequadamente a base de cálculo reduzida do ISS Municipal sem o percentual aplicável.
