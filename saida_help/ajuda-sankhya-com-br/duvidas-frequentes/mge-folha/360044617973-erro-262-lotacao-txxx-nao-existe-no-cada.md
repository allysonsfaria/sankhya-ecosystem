---
id: "360044617973"
titulo: "Erro 262 - Lotação 'TXXX' não existe no cadastro do empregador para o período '201Y-YY'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044617973-Erro-262-Lota%C3%A7%C3%A3o-TXXX-n%C3%A3o-existe-no-cadastro-do-empregador-para-o-per%C3%ADodo-201Y-YY"
trilha: "Dúvidas Frequentes > MGE Folha"
atualizado_em: "2026-07-29T13:33:50Z"
rotulos: ["#RevisadoLorrana", "Configuração", "Parceiro", "eSocial", "Lotação Não Encontrada no Cadastro do Empregador", "Erro", "Central de Projetos"]
---

# Erro 262 - Lotação 'TXXX' não existe no cadastro do empregador para o período '201Y-YY'

**![Imagem 1: MENSAGEM (Erro 262): Lotação 'TXXX' não existe no cadastro do empregador para o período '201Y-YY'. Ação Sugerida: O…](https://ajuda.sankhya.com.br/hc/article_attachments/16941688855319) MENSAGEM**[Erro 262]: Lotação 'TXXX' não existe no cadastro do empregador para o período '201Y-YY'.
Ação Sugerida: O valor informado no campo Código de Lotação deverá existir na Tabela de Lotações Tributárias, informada pelo empregador. 
Elemento: /eSocial/evtRemun/dmDev/  infoPerApur/ideEstabLot/  codLotacao [TXXX]

**![Imagem 2: SITUAÇÃO : Ao enviar a folha de pagamento no evento S-1200, informa que a lotação não foi localizada. Lotação não foi…](https://ajuda.sankhya.com.br/hc/article_attachments/16941695115671) SITUAÇÃO**: 
Ao enviar a folha de pagamento no evento S-1200, informa que a lotação não foi localizada. 
Lotação não foi gerada conforme esperado.

**![Imagem 3: SOLUÇÃO](https://ajuda.sankhya.com.br/hc/article_attachments/16941695121687) SOLUÇÃO**

Para correção, siga os passos abaixo:

![Imagem 4: Acesse: MGEPessoal » Lançamentos » Movimentação de Tomadores de Serviço](https://ajuda.sankhya.com.br/hc/article_attachments/16941688872471) Acesse: MGEPessoal » Lançamentos » Movimentação de Tomadores de Serviço

Localize o funcionário e confira o código de tomador de serviço vinculado no período.

![Imagem 5: Acesse: MGEPessoal » Arquivos » Parceiros](https://ajuda.sankhya.com.br/hc/article_attachments/16941688890903) Acesse: MGEPessoal » Arquivos » Parceiros

Localize nessa tela o código do tomador de serviço. Na aba **"Tomador"**, campo **"Tipo de lotação"**, vincule o tipo de lotação conforme Anexo I, dos Leiautes do eSocial - Tabela 10 - Tipos de Lotação Tributária.

![Imagem 6: Acesse: MGEPessoal » Avançado » Preferências » Todas as Preferências](https://ajuda.sankhya.com.br/hc/article_attachments/16941695141143) Acesse: MGEPessoal » Avançado » Preferências » Todas as Preferências

Parâmetro **"FPESOCIALDEPTOM"** deve estar desligado quando tratar-se de empresa com tomador de serviço.

**![Imagem 7: Parâmetro "FPESOCIALDEPTOM" deve estar desligado quando tratar-se de empresa com tomador de serviço. CAUSA : Mensagem…](https://ajuda.sankhya.com.br/hc/article_attachments/16941688901911) CAUSA**:
Mensagem apresentada quando o tomador não foi enviado ao eSocial e o parâmetro FPESOCIALDEPTOM está ligado. O parâmetro FPESOCIALDEPTOM só deve ser ligado quando tratar-se de obra própria.
