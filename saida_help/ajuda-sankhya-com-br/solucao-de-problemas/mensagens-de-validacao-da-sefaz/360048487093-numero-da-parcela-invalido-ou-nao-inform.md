---
id: "360048487093"
titulo: "Número da parcela inválido ou não informado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360048487093-N%C3%BAmero-da-parcela-inv%C3%A1lido-ou-n%C3%A3o-informado"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T15:31:50Z"
rotulos: ["Configuração", "NF-e", "XML", "SEFAZ", "UFNFEOMITV160B", "852", "nDup", "Número da Parcela Inválido", "Erro", "Documentos Eletrônicos"]
---

# Número da parcela inválido ou não informado

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16311421628439) MENSAGEM:**

[852 - Rejeição]: Número da parcela inválido ou não informado

![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16311410094743) **SOLUÇÃO:**

![Imagem 3: Certifique-se que a UF emissora da nota não consta no parâmetro abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/16311410111511) Certifique-se que a UF emissora da nota não consta no parâmetro abaixo:

- Tela **"[Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias)"** (Caminho para acesso: Configurações » Avançado » Preferências), parâmetro Chave **"UFNFEOMITV160B - UFs que omitem o schema NFe 4.0 v1.60B"**:

![Imagem 4: Tela " Preferências " (Caminho para acesso: Configurações » Avançado » Preferências), parâmetro Chave "UFNFEOMITV160B -…](https://ajuda.sankhya.com.br/hc/article_attachments/14439243628823)

Foi criado o parâmetro UFNFEOMITV160B com default vazio. Essa criação ocorreu quando algumas UFs ainda estavam com sua SEFAZ sem implementar esse schema.

![Imagem 5: Após retirar a UF do parâmetro, refaça o faturamento. Gere o XML em conferência e certifique-se que a tag <nDup> foi…](https://ajuda.sankhya.com.br/hc/article_attachments/16311410114327) Após retirar a UF do parâmetro, refaça o faturamento. Gere o XML em conferência e certifique-se que a tag **<nDup>** foi gerada seguindo as regras da SEFAZ:

**(2)** O número de parcelas deve ser informado com 3 algarismos, sequenciais e consecutivos. Exemplo: **"001", "002", "003"**

![Imagem 6: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16311421643671)**OBSERVAÇÃO:** 

Nota Técnica (**NT-2016.002 - v 1.60**):

**<http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=Y6Lj7G0uHwc=>**

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16311410122135) CAUSA:**

Se informado o Grupo de Parcelas de cobrança (tag <dup>), Número da parcela (<nDup>) não informado ou inválido.

![Imagem 8: OBSERVAÇÃO: O número de parcelas deve ser informado com 3 algarismos, sequenciais e consecutivos. Exemplo: "001",…](https://ajuda.sankhya.com.br/hc/article_attachments/16311421643671)**OBSERVAÇÃO:** 
O número de parcelas deve ser informado com 3 algarismos, sequenciais e consecutivos. Exemplo: "001", "002", "003", ...
