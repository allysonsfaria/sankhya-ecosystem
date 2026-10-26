---
id: "18786665647511"
titulo: "909 Rejeição: Obrigatório o preenchimento de Grupo de Tributacao do ICMS monofasica sobre combustiveis [nItem:x]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/18786665647511-909-Rejei%C3%A7%C3%A3o-Obrigat%C3%B3rio-o-preenchimento-de-Grupo-de-Tributacao-do-ICMS-monofasica-sobre-combustiveis-nItem-x"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:52:06Z"
rotulos: ["Configuração", "NF-e", "XML", "SEFAZ", "ICMS", "Impostos", "Estoque", "Rastreamento de Estoque", "Rejeição 909", "Grupo de Tributação do ICMS", "Passos para resolver", "Erro", "Como Resolver", "ICMS monofasica sobre combustiveis"]
---

# 909 Rejeição: Obrigatório o preenchimento de Grupo de Tributacao do ICMS monofasica sobre combustiveis [nItem:x]

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18786665635351) **MENSAGEM:**

909 Rejeição: Obrigatório o preenchimento de Grupo de Tributacao do ICMS monofasica sobre combustiveis [nItem:x]

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18786645318935)SOLUÇÃO:**

**(1)** Realize a consulta abaixo para verificar se produto tem rastreio de estoque ST.

SELECT UFS.UF, UFS.CODIBGE, MAX(VAS.NUNOTAORIG) FROM TGFVAS VAS
INNER JOIN TGFITE ITE ON ITE.NUNOTA = VAS.NUNOTAORIG AND ITE.SEQUENCIA = VAS.SEQUENCIAORIG
INNER JOIN TGFCAB CAB ON CAB.NUNOTA = ITE.NUNOTA
INNER JOIN TGFPAR PAR ON PAR.CODPARC = CAB.CODPARC
INNER JOIN TSIUFS UFS ON UFS.CODUF = (SELECT CID.UF FROM TSICID CID WHERE CID.CODCID = PAR.CODCID)
WHERE ITE.CODPROD = XXXX  AND VAS.NUNOTA = XXXX
GROUP BY UFS.UF, UFS.CODIBGE
ORDER BY 3 DESC

**(2)** Para que o grupo de TAGs seja gerado corretamente no XML da NF-e, acesse a tela **“Produtos”** (Configurações » Cadastros » Produtos » Produtos) e verifique se os produtos classificados como gás estão devidamente configurados.

**(3)** Na aba **''Rastreamento por Empresa''** confirme:

- O **código da empresa** incluído;
- O campo **“Tipo de Rastreamento”** deve estar definido como **“RASTREAR”**, conforme imagem abaixo:

![Imagem 3: O campo “Tipo de Rastreamento” deve estar definido como “RASTREAR” , conforme imagem abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/19056427087511)

**(4)** Além da configuração no cadastro do produto, o processo de rastreamento deve estar ativado no sistema por meio da tela **“Ativar/Reprocessar Rastreamento de Estoque/ST”** (Livros Fiscais » Avançado » Rastreamento de Estoque/ST » Ativar/Reprocessar Rastreamento de Estoque/ST).

![Imagem 4: (4) Além da configuração no cadastro do produto, o processo de rastreamento deve estar ativado no sistema por meio da…](https://ajuda.sankhya.com.br/hc/article_attachments/19056436331543)

**(5)** Após selecionar o **produto** e a **empresa** desejados, clique em **“Processar”** para efetivar a configuração. O processamento deve ser concluído **sem retornar nenhum erro**.

**(6)** Após a execução correta, o XML deverá gerar o grupo de TAGs conforme exemplo abaixo:

```
<origComb>
   <indImport>0</indImport>
   <cUFOrig>43</cUFOrig>
   <pOrig>100.0</pOrig>
</origComb>
```

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18786645321239)CAUSA:**

O produto não está com o processo **“Ativar/Reprocessar Rastreamento de Estoque/ST”** ativo no sistema. Nessa situação, o grupo de TAGs não é gerado no XML, ocasionando rejeição na validação.

**OBSERVAÇÃO:**

Quando a nota for do **tipo de movimento Transferência**, além das configurações mencionadas anteriormente, é necessário que o campo **“Atualização de Livro ICMS”** esteja configurado como **“Ambos”**, conforme a imagem abaixo:

![Imagem 6: Quando a nota for do tipo de movimento Transferência , além das configurações mencionadas anteriormente, é necessário…](https://ajuda.sankhya.com.br/hc/article_attachments/19056427107735)

Se for:

- **Nota de venda** → o campo deve estar marcado como **“Livro de Saída”**;
- **Nota de compra** → o campo deve estar marcado como **“Livro de Entrada”**.

Para mais detalhes sobre o processo de rastreamento, consulte a documentação [**''Rastreabilidade de Estoque/ICMS-ST''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/5818008318231)**.**
