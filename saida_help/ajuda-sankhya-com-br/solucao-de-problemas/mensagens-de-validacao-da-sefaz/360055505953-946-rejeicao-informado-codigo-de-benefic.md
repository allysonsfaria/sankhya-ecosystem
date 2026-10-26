---
id: "360055505953"
titulo: "946 Rejeição: Informado código de benefício fiscal incorreto ou inexistente na UF"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360055505953-946-Rejei%C3%A7%C3%A3o-Informado-c%C3%B3digo-de-benef%C3%ADcio-fiscal-incorreto-ou-inexistente-na-UF"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T15:28:26Z"
rotulos: ["Configuração", "NF-e", "XML", "SEFAZ", "Impostos", "não apagar", "Benefício Fiscal: Correção Necessária", "Verificar e Ajustar", "Refaturamento Requerido", "Erro", "946 Rejeição", "Rejeição 946", "Informado código de benefício fiscal incorreto ou inexistente na UF"]
---

# 946 Rejeição: Informado código de benefício fiscal incorreto ou inexistente na UF

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/15853945962135) MENSAGEM**:

946 Rejeição: Informado código de benefício fiscal incorreto ou inexistente na UF.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/15853945963543) SOLUÇÃO:**

![Imagem 3: Gerar o XML em conferência e verificar a informação apresentada na tag cBenef:](https://ajuda.sankhya.com.br/hc/article_attachments/15853940333591) Gerar o XML em conferência e verificar a informação apresentada na tag **`cBenef:`**

- Verificar se o **código do benefício fiscal existe e está vigente** (conforme Tabela de código de benefício fiscal por UF publicada na Secretaria da Fazenda da respectiva UF).

**Tabela disponível em**:

https://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=Iy/5Qol1YbE=![Imagem 4: https://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=Iy/5Qol1YbE=](https://ajuda.sankhya.com.br/hc/article_attachments/360097557253)

![Imagem 5: Ajuste o cadastro do respectivo código benefício em seu sistema para o código correto (Tela 'Cadastro Benefícios').…](https://ajuda.sankhya.com.br/hc/article_attachments/15853940334359) Ajuste o cadastro do respectivo código benefício em seu sistema para o código correto (Tela 'Cadastro Benefícios'). Para mais detalhes sobre como esse cadastro é realizado, acesse:

[Melhores práticas para utilização do 'Código Benefício' por Produto/Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043986434)

![Imagem 6: Feito o ajuste, refaça o faturamento.](https://ajuda.sankhya.com.br/hc/article_attachments/15853940334999) Feito o ajuste, refaça o faturamento.

**![Atenção](https://ajuda.sankhya.com.br/guide-media/01H4R46RFFDEZMCB2FRR2NW2PM) Importante:**

Para geração da tag <cBenef> são permitidos 10 caracteres conforme a NT 2016.002, porém há casos em que a UF do Emitente permite apenas 8. Sendo assim, a UF do Emitente que permite apenas 8 caracteres deve estar informada no parâmetro **UFPER8CTAGCBENE** - 'UFs permitem o envio de 8 caracteres na tag cBenef.

- Tela 'Preferências' (Configurações » Avançado » Preferências)
- Chave: **UFPER8CTAGCBENE**

![Imagem 8: Chave: UFPER8CTAGCBENE](https://ajuda.sankhya.com.br/hc/article_attachments/360097558653)

**![Imagem 9: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/15853945975703) CAUSA:**

Quando emitida uma NF-e (modelo 55) ou NFC-e (modelo 65) e informado o código de benefício fiscal (Campo: **cBenef**) inexistente ou fora do prazo de vigência de acordo com a Tabela de Código de Benefício Fiscal por UF.

**Implementação a critério da UF e por modelo de DF-e.**

- Exceção 1: a RV não se aplica quando Finalidade de emissão da NFe (tag: finNFe) igual a Devolução de Mercadoria e Identificador de local de destino da operação (tag: idDest) igual a Operação interestadual ou com o Exterior.
- Exceção 2: a critério da UF, a RV não se aplica quando Finalidade de emissão da NF-e (tag: finNFe) igual a Devolução de Mercadoria;
- Exceção 3: a critério da UF, a RV não se aplica quando Finalidade de emissão da NF-e (tag: finNFe) igual a NF-e de Ajuste;
- Exceção 4: a critério da UF, a RV não se aplica quando Tipo de Operação (tag: tpNF) igual à Entrada.
- Exceção 5: essa RV não se aplica quando informado CSOSN (operação realizada por optante pelo Simples Nacional);
