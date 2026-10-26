---
id: "37808779732503"
titulo: "Como lançar atestado médico recorrente"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37808779732503-Como-lan%C3%A7ar-atestado-m%C3%A9dico-recorrente"
trilha: "Manual do Produto > Pessoas+ > Afastamentos e Ocorrências > Lançamento de Afastamentos e Atestados"
atualizado_em: "2026-10-02T15:31:36Z"
rotulos: ["Ocorrências", "eSocial", "Folha de Pagamento", "Lançamento de ocorrências", "Pessoal+", "ID: br.com.sankhya.rh.LancamentoOcorrencias", "Atestado Médico"]
---

# Como lançar atestado médico recorrente

**Módulo:** Pessoal+
**Caminho de acesso:** Pessoal+ > Rotinas Folha > Ocorrências
**ID da Tela:** br.com.sankhya.rh.LancamentoOcorrencias

---

### Descrição e Usabilidade

O cadastro de atestado recorrente é utilizado quando um colaborador apresenta um novo afastamento relacionado ao mesmo CID (Classificação Internacional de Doenças) dentro do período de 60 dias após o retorno de um afastamento anterior.

Nesses casos, o sistema permite vincular o novo atestado ao anterior por meio da opção **É Recorrente**, garantindo o tratamento correto da ocorrência nos cálculos da folha e afastamentos.

Esse vínculo é importante para:

- evitar pagamento indevido dos 15 primeiros dias pela empresa;
- garantir o correto cálculo da Parte Empresa Afastamentos;
- manter o histórico de reincidência do afastamento;
- assegurar consistência nas informações previdenciárias.

| **⚠️** **Atenção**  Quando o atestado recorrente não é vinculado corretamente ao afastamento anterior, o cálculo da folha pode apresentar inconsistências nos afastamentos. |
| --- |

### Pré-requisitos

Antes de realizar o cadastro do atestado recorrente, verifique:

- existência do afastamento anterior já lançado no sistema;
- que o novo afastamento possui o mesmo CID;
- que o novo afastamento ocorreu dentro de 60 dias após o retorno do afastamento anterior;
- permissão de acesso à rotina **Ocorrências** (Pessoal+ > Rotinas Folha). Essa liberação é feita na tela **Acessos** (Configurações > Controle de Acesso), pelo administrador do sistema.

### Jornada de Uso

[GIF animado: Imagem 1: Jornada de Uso](https://ajuda.sankhya.com.br/hc/article_attachments/40384779018519)

1. Após a entrega do atestado pelo colaborador, acesse a tela **Ocorrências** (Pessoal+ > Rotinas Folha);
2. Utilize o painel de filtros lateral para facilitar a busca do colaborador, selecione:

   - **Empresa**;
   - **Tipo de filtro**.
3. Clique em **Pesquisar**, o card do colaborador será exibido;
4. Inicie o lançamento da ocorrência clicando em **Ativa Seleção para lançamento**;
5. Clique no card do colaborador para selecioná-lo;
6. Clique no botão **Lançar ocorrência;**
7. Escolha a ocorrência desejada e clique sobre ela;
8. Clique em **Adicionar Arquivo** para incluir para inserir o documento comprobatório:

   - atestado médico;
   - laudo;
   - documento comprobatório do afastamento.
9. Clique em **Lançar ocorrência**;
10. Preencha os dados do afastamento:

    - **Descrição da ocorrência**;
    - **Data de Início**;
    - **Data prevista de retorno** ou **Data de término**;
    - **Dias de afastamento previstos** (quando necessário).

      O campo **Dias de Afastamento Previstos** é preenchido automaticamente quando você informa a **Data prevista de retorno**. Se preferir, ao preencher o número de **Dias de Afastamento Previstos**, o sistema calculará a **Data prevista de retorno** com base na **Data de Início**.
11. Marque a opção **É Recorrente**;

    O sistema exibirá os atestados anteriores disponíveis para vínculo;
12. Selecione o atestado correspondente ao afastamento anterior;

    **É obrigatório** selecionar o atestado anterior exibido na lista. Somente marcar a opção **É Recorrente** sem realizar o vínculo não caracteriza corretamente a reincidência.

    Após selecionar o atestado anterior, o sistema exibirá automaticamente o **Número de Ocorrência Reincidente**.

    | **⚠️** **Atenção**  Esse vínculo garante o correto tratamento do afastamento nos cálculos da folha. |
    | --- |

    | 🚨 **Correção da recorrência após o lançamento - versão > 5.116**  Se a opção **É Recorrente** não tiver sido marcada ou a ocorrência anterior tiver sido vinculada incorretamente, é possível editar essas informações posteriormente na ocorrência já lançada.  A edição seguirá as mesmas regras utilizadas no lançamento da ocorrência, inclusive quanto às ocorrências disponíveis para vinculação.  **⚠️** Não será possível editar esse campo quando existir cálculo de folha processado para o período da ocorrência. Nesse caso, exclua o cálculo para habilitar novamente a edição. |
    | --- |
13. Clique em **Atestado**, escolha o **colaborador**, preencha os dados do médico, o **CID** e os dias de afastamento, e confirme;

    | **⚠️** **Atenção**  O botão **Confirmar lançamento** será habilitado somente após o preenchimento dos campos obrigatórios. |
    | --- |
14. Revise as informações e clique em **Confirmar lançamento**;
15. Após o retorno do colaborador:

    - acesse novamente a ocorrência;
    - preencha a Data de término do afastamento.

    | **⚠️** **Atenção**  Em afastamentos pelo INSS, a **Data de término** deve ser preenchida somente quando o colaborador retornar efetivamente ao trabalho. |
    | --- |

### Pontos de Atenção

- O vínculo recorrente somente pode ser realizado com atestados dos últimos 60 dias.
- O CID do novo afastamento deve corresponder ao afastamento anterior.
- Não vincular corretamente o atestado recorrente pode gerar inconsistências na Parte Empresa Afastamentos.
- O preenchimento incorreto das datas pode impactar:
  - cálculos da folha;
  - afastamentos;
  - férias;
  - encargos previdenciários.
- A Data prevista de retorno deve ser utilizada quando ainda não existir uma Data de término definida.
- O sistema apresenta somente ocorrências do mesmo colaborador que atendam às regras de vinculação da recorrência.

### Perguntas Frequentes (FAQ)

**1. Quando devo utilizar a opção É Recorrente?**

Quando o colaborador apresentar novo afastamento pelo mesmo CID dentro de 60 dias após o retorno do afastamento anterior.

**2. Apenas marcar a opção É Recorrente é suficiente?**

Não. É obrigatório selecionar o atestado anterior exibido pelo sistema para criar o vínculo de reincidência.

**3. O que acontece se eu não vincular o atestado anterior?**

O cálculo da folha poderá considerar incorretamente a responsabilidade pelos dias de afastamento, impactando a Parte Empresa Afastamentos.

**4. O sistema mostra qualquer afastamento anterior?**

Não. Apenas afastamentos compatíveis com as regras de reincidência serão exibidos.

**5. Preciso informar Data de Término no lançamento inicial?**

Não obrigatoriamente. Quando o retorno ainda não ocorreu, utilize a Data prevista de retorno.

**6. Posso anexar documentos no lançamento?**

Sim. É possível anexar atestados médicos e demais documentos comprobatórios.

**7. O que acontece se o novo afastamento ocorrer após 60 dias?**

Nesse caso, ele não será tratado como recorrente.

**8. Por que não consigo marcar um atestado como recorrente?**

A opção **É Recorrente** pode não estar disponível por dois motivos:

- não existe, para o colaborador, uma ocorrência anterior que atenda às regras para vinculação;
- existe cálculo de folha processado para o período da ocorrência que está sendo editada.

Nesse último caso, exclua o cálculo da folha para habilitar novamente a edição.

**9. Posso corrigir a recorrência depois de lançar a ocorrência?**

Sim. É possível editar a ocorrência já lançada e alterar a opção **É Recorrente** e a **Ocorrência anterior**, desde que não exista cálculo de folha processado para o período da ocorrência.

A ocorrência anterior disponível para seleção seguirá as mesmas regras utilizadas no lançamento.

### Artigos Relacionados

- [Cadastro de Ocorrências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044610494)
- [Lançamento de Atestado Médico](https://ajuda.sankhya.com.br/hc/pt-br/articles/40388499298071)
- [Consulta de Ocorrências Lançadas para o Colaborador](https://ajuda.sankhya.com.br/hc/pt-br/articles/40336545146519)
- [Edição de Ocorrências Lançadas para o Colaborador](https://ajuda.sankhya.com.br/hc/pt-br/articles/40407377343127)
- [Exclusão de Ocorrências Lançadas para o Colaborador](https://ajuda.sankhya.com.br/hc/pt-br/articles/40407825863319)
- [Cálculo da Folha de Pagamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/39309113368599)
- [Gerenciador de Folhas](https://ajuda.sankhya.com.br/hc/pt-br/articles/40106318532247)
