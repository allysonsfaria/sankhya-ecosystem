---
id: "40388499298071"
titulo: "Como lançar atestado médico para um colaborador"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/40388499298071-Como-lan%C3%A7ar-atestado-m%C3%A9dico-para-um-colaborador"
trilha: "Manual do Produto > Pessoas+ > Afastamentos e Ocorrências > Lançamento de Afastamentos e Atestados"
atualizado_em: "2026-10-02T15:30:31Z"
rotulos: ["Ocorrências", "br.com.sankhya.rh.LancamentoOcorrencias", "eSocial", "Folha de Pagamento", "Configuração Funcionários", "Pessoal+", "Lançamento de atestado médico recorrente", "Atestado Médico em Dias", "CID 10", "Atestado Médico"]
---

# Como lançar atestado médico para um colaborador

**Módulo:** Pessoal+
**Caminho de acesso:** Pessoal+ > Rotinas Folha > Ocorrências
**ID da Tela:** br.com.sankhya.rh.LancamentoOcorrencias

---

### Descrição e Usabilidade

A rotina de lançamento de atestado médico permite registrar afastamentos temporários dos colaboradores por motivo de saúde, garantindo o correto tratamento das informações trabalhistas, previdenciárias e de cálculo da folha.

O lançamento correto do atestado é importante para:

- controle de afastamentos;
- cálculo da folha de pagamento;
- controle de dias afastados;
- integração com férias e encargos;
- envio correto das informações ao eSocial.

Este artigo contempla o lançamento de atestados médicos comuns, sem vínculo de recorrência.

📚 Para afastamentos relacionados ao mesmo CID dentro de 60 dias após o retorno do colaborador, consulte o artigo de [Lançamento de atestado médico recorrente](https://ajuda.sankhya.com.br/hc/pt-br/articles/37808779732503).

### Pré-requisitos

Antes de realizar o lançamento, verifique:

- Permissões de acesso à rotina Ocorrências;
- Cadastro do colaborador ativo;
- Documento do atestado médico disponível para conferência ou anexo.

### Jornada de Uso

[GIF animado: Imagem 1: Jornada de Uso](https://ajuda.sankhya.com.br/hc/article_attachments/40388866068503)

1. Após a entrega do atestado pelo colaborador, acesse a tela **Ocorrências** (Pessoal+ > Rotinas Folha);
2. Utilize o painel de filtros lateral para facilitar a busca do colaborador, selecione:

   - **Empresa**;
   - **Tipo de filtro**.
3. Clique em **Pesquisar**, o card do colaborador será exibido;
4. Inicie o lançamento da ocorrência clicando em **Ativa Seleção para lançamento**;
5. Clique no card do colaborador para selecioná-lo;
6. Clique no botão**Lançar ocorrência;**
7. Escolha a ocorrência desejada e clique sobre ela;
8. Clique em **Adicionar Arquivo** para incluir para inserir o documento comprobatório:

   - atestado médico;
   - laudo;
   - documento comprobatório do afastamento.
9. Clique em**Lançar ocorrência**;
10. Preencha os dados do afastamento:

    - **Descrição da ocorrência**;
    - **Data de Início**;
    - **Data prevista de retorno** ou **Data de término**;
    - **Dias de afastamento previstos** (quando necessário).
    - O campo **Dias de Afastamento Previstos** é preenchido automaticamente quando você informa a **Data prevista de retorno**. Se preferir, ao preencher o número de **Dias de Afastamento Previstos**, o sistema calculará a **Data prevista de retorno** com base na **Data de Início**.

      ⚠️ Neste cenário, não marque a opção **É Recorrente**.
11. Clique em **Atestado** para informar:

    - dados do médico responsável;
    - CID e os dias de afastamento, e confirme.

    ⚠️O botão **Confirmar lançamento** será habilitado somente após o preenchimento dos campos obrigatórios.
12. Revise as informações e clique em **Confirmar lançamento**;
13. Após o retorno do colaborador:

    - acesse novamente a ocorrência;
    - preencha ou revise a **Data de término** do afastamento.

      | **⚠️** **Atenção**  O preenchimento de atestados de até 15 dias deve incluir **Data de Início** e **Data de término**. O campo **Data prevista de retorno** é usado só para afastamentos pelo INSS, pois pode haver prorrogação.  Em afastamentos pelo INSS, a **Data de término** deve ser preenchida somente quando o colaborador retornar efetivamente ao trabalho. |
      | --- |

### Pontos de Atenção

- Não marque a opção **É Recorrente** para atestados sem reincidência.
- O preenchimento incorreto das datas pode impactar:
  - cálculos da folha;
  - férias;
  - encargos;
  - afastamentos previdenciários.
- Quando um **atestado médico comum tiver início durante o período de férias do colaborador**, os dias coincidentes com as férias não interrompem nem suspendem automaticamente o período de descanso.

  Nessas situações, o lançamento do afastamento deve considerar apenas os dias do atestado que permanecerem vigentes após o término das férias.

  **Exemplo:**

  - Férias: 09/05/2026 a 08/06/2026
  - Atestado médico: 28/05/2026 a 27/06/2026

  Neste cenário:

  - O período de 28/05/2026 a 08/06/2026 permanece registrado como férias;
  - O afastamento médico deverá ser lançado a partir de 09/06/2026;
  - O afastamento permanecerá vigente até 27/06/2026.

  Esse procedimento evita sobreposição entre períodos de férias e afastamento médico e garante o tratamento correto das informações na folha de pagamento e nos eventos do eSocial.
- Utilize **Data prevista de retorno** quando ainda não houver retorno efetivo.
- Sempre valide o período informado no documento médico antes da confirmação.
- O anexo do documento comprobatório ajuda na rastreabilidade e auditoria do afastamento.

### Perguntas Frequentes (FAQ)

**1. Posso anexar o atestado médico?**

Sim. O sistema permite anexar documentos comprobatórios diretamente no lançamento.

**2. O preenchimento da Data de Término é obrigatório?**

Não inicialmente. Ela pode ser preenchida posteriormente no retorno do colaborador.

**3. O sistema calcula automaticamente os dias de afastamento?**

Sim. Quando a Data prevista de retorno é informada.

**4. O atestado impacta a folha de pagamento?**

Sim. O afastamento pode impactar cálculos, encargos e controle de afastamentos.

**5. Posso editar o afastamento após o lançamento?**

Sim, desde que o cálculo da folha ainda permita alterações.

**6. Como lançar um atestado que começou durante as férias do colaborador?**

Se o atestado iniciar durante o período de férias, os dias coincidentes com as férias devem permanecer registrados como férias. O afastamento deve ser lançado apenas a partir do primeiro dia após o término das férias, considerando os dias restantes do atestado.

### Artigos Relacionados

- [Cadastro de Ocorrências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044610494)
- [Lançamento de Atestado Médico Recorrente](https://ajuda.sankhya.com.br/hc/pt-br/articles/37808779732503)
- [Consulta de Ocorrências Lançadas para o Colaborador](https://ajuda.sankhya.com.br/hc/pt-br/articles/40336545146519)
- [Edição de Ocorrências Lançadas para o Colaborador](https://ajuda.sankhya.com.br/hc/pt-br/articles/40407377343127)
- [Exclusão de Ocorrências Lançadas para o Colaborador](https://ajuda.sankhya.com.br/hc/pt-br/articles/40407825863319)
- [Cálculos da Folha de Pagamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/39309113368599)
- [Gerenciador de Folhas](https://ajuda.sankhya.com.br/hc/pt-br/articles/40106318532247)
