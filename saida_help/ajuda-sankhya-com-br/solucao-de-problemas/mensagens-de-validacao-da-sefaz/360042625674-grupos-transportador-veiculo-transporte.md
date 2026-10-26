---
id: "360042625674"
titulo: "Grupos Transportador, Veiculo Transporte e Reboque não devem ser informados (NT2016/002)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042625674-Grupos-Transportador-Veiculo-Transporte-e-Reboque-n%C3%A3o-devem-ser-informados-NT2016-002"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:08:25Z"
rotulos: ["ERRONF", "Configuração", "NF-e", "XML", "SEFAZ", "Transporte", "868", "Erro: Dados de transporte", "Solução: Remover informações.", "Configuração: Preferências da empresa", "NT2016/002"]
---

# Grupos Transportador, Veiculo Transporte e Reboque não devem ser informados (NT2016/002)

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16503960110103) MENSAGEM:**

[868 - Rejeição]: Grupos Transportador, Veiculo Transporte e Reboque não devem ser informados (NT2016/002)

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16503960112151)SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Acesse a aba "Transporte" do rodapé da nota e verifique os dados do Veículo (Placa e UF), onde a operação for…](https://ajuda.sankhya.com.br/hc/article_attachments/16503939503895) Acesse a aba **"Transporte"** do rodapé da nota e verifique os dados do Veículo (Placa e UF), onde a operação for Interestadual, retire essas informações da nota.

Há algumas observações importantes que devem ser ressaltadas:

- A critério de cada UF, a regra de validação acima também pode ser aplicada nas operações internas (idDest=1) se código do município (cMun) do Emitente for diferente do código do município (cMun) do Destinatário;
- Esta regra não se aplica a emissão da NFA-e.

![Imagem 4: Nas preferências da empresa, (Caminho de acesso: Comercial » Preferências » Empresa ), aba "Propriedades" , temos o…](https://ajuda.sankhya.com.br/hc/article_attachments/16503960115607) Nas preferências da empresa, (Caminho de acesso: Comercial » Preferências » Empresa), aba **"Propriedades"**, temos o seguinte campo:**"Gerar as informações do Grupos Veículo Transporte e Grupo Reboque:",** através deste campo configura-se em quais operações serão geradas as tags referentes aos Grupos Veículo Transporte e Reboque no XML da nota. São apresentadas as seguintes opções:

- **Dentro do Município**: Optando-se por essa opção, o sistema irá gerar as tags no XML apenas para as notas onde o parceiro esteja localizado no mesmo município da empresa;
- **Dentro do Estado:** O sistema irá gerar as tags do XML da nota somente quando o parceiro e a empresa estiverem no mesmo Estado;
- **Todas as operações:** Independente da localização da empresa ou do parceiro, caso as informações do "Grupo de Veículo e Grupo Reboque" estejam preenchidas na nota, o sistema irá gerar as tags no XML.

![Imagem 5: Após os ajustes, gere novamente o lote da NF-e.](https://ajuda.sankhya.com.br/hc/article_attachments/16503960116631) Após os ajustes, gere novamente o lote da NF-e.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16503939513111)CAUSA:**

Quando for emitida uma NF-e (modelo 55) com Operação de Destino igual a **"2 - Interestadual"** e for informado os Grupos Veiculo Transporte e Reboque, será retornada a rejeição.

**![Imagem 7: OBSERVAÇÕES:](https://ajuda.sankhya.com.br/hc/article_attachments/16503939515799)OBSERVAÇÕES:**

**(1)** Nos casos de operação interestadual ou interna em alguns casos, quando o município de origem for diferente do de destino, é necessária a emissão do MDF-e e neste documento devem constar os dados do Transportador e veículo transportado.

**(1)**([NT2016/002](http://www.nfe.fazenda.gov.br/portal/Exibirarquivo.aspx?conteudo=c4S6yXTKpXY=)) - Nota Técnica.
