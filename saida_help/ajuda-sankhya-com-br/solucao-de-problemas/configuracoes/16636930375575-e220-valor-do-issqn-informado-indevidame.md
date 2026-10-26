---
id: "16636930375575"
titulo: "E220: Valor do ISSQN informado indevidamente e E221: Aliquota informada indevidamente. Possível solução"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/16636930375575-E220-Valor-do-ISSQN-informado-indevidamente-e-E221-Aliquota-informada-indevidamente-Poss%C3%ADvel-solu%C3%A7%C3%A3o"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-10-02T15:00:09Z"
rotulos: ["Configuração", "Alíquota de ISS", "XML", "Impostos", "Prefeituras", "NFS-e", "ISSQN", "Solução para Erros E220 e E221"]
---

# E220: Valor do ISSQN informado indevidamente e E221: Aliquota informada indevidamente. Possível solução

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16636942161303)  MENSAGEM:**

E220: Valor do ISSQN informado indevidamente. Possível solução: O valor do ISSQN será calculado pela Prefeitura e não deve ser informado pelo contribuinte.

E221: Alíquota informada indevidamente. Possível solução: A alíquota do ISSQN só deve ser informada quando: o ISSQN for devido a outro município ou o prestador do serviço for optante pelo Simples Nacional e houver retenção do ISSQN. Em outras situações a alíquota a ser aplicada será determinada pela Prefeitura.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16636899305239) CAUSA:**

O Valor do ISS esta sendo informado no XML através da TAG  <ValorIss>e a prefeitura não aceita que seja calculado.

![Imagem 3: O Valor do ISS esta sendo informado no XML através da TAG <ValorIss>e a prefeitura não aceita que seja calculado.](https://ajuda.sankhya.com.br/hc/article_attachments/18979960406039)

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16636940403863)SOLUÇÃO:**

Marque o campo "Envia o ValorISS e alíquota no XML, apenas quando o ISS for devido a outro município?" **Empresa** (Comercial » Preferências » Empresa) aba Documentos Fiscais Eletrônicos » NFS-e.

**![Imagem 5: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16676674699159) OBSERVAÇÃO:**

Quando a marcação **"Envia o ValorISS e alíquota no XML, apenas quando o ISS for devido a outro município?"** estiver ligada, o sistema enviará as tags ValorISS e Alíquota no XML somente se a tag <municipioincidência> for diferente do município da empresa.

![Imagem 6: Quando a marcação "Envia o ValorISS e alíquota no XML, apenas quando o ISS for devido a outro município?" estiver…](https://ajuda.sankhya.com.br/hc/article_attachments/30097074505495)

Após a Marcação do campo, gere o lote da nota novamente e verifique se no XML não ira mais constar o a TAG <ValorIss>.

![Imagem 7: Após a Marcação do campo, gere o lote da nota novamente e verifique se no XML não ira mais constar o a TAG <ValorIss>.](https://ajuda.sankhya.com.br/hc/article_attachments/18979960422039)

Confira mais informações no manual das [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abanfs-e)
