---
id: "42427325846167"
titulo: "R01 - Como gerar o espelho de ponto de vários colaboradores"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427325846167-R01-Como-gerar-o-espelho-de-ponto-de-v%C3%A1rios-colaboradores"
trilha: "PONTOTEL: Sistema de marcação de ponto > Relatórios, Importadores e Exportadores"
atualizado_em: "2026-08-03T13:29:33Z"
rotulos: ["sync_hc", "pontotel", "pontotel_6a33edeb4c9ca3458ae83eef", "sync_hash_9b6c73d45909"]
---

# R01 - Como gerar o espelho de ponto de vários colaboradores

O espelho da folha de ponto é um relatório essencial para a gestão de registros trabalhistas. Ele detalha os pontos, apontametnos e outros eventos da jornada de trabalho dos colaboradores, garantindo maior transparência e conformidade com a legislação. A emissão desse relatório é importante para auditar inconsistências, validar informações com os colaboradores e assegurar que os dados estejam corretos antes do fechamento da folha.

Seguindo os passos informados abaixo, você poderá emitir os espelhos de ponto de vários colaboradores em um único processo, facilitando o acompanhamento e a análise. Confira abaixo como gerar o relatório R01 de forma simples e eficiente.

---

## Como gerar o relatório R01 em massa

1. No menu de navegação do [site Gestão](https://gestao.pontotel.com.br/), selecione a opção **Relatórios e Registros**.
2. Na nova tela, selecione a opção "**R01 - Espelho/Folha de pontos de todos os empregados**".
3. Configure os **filtros** do relatório.

![Imagem 1: Configure os filtros do relatório.](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_1ydgcz6.png)

**3.1.Seção: Locais de trabalho, empregadores ou grupos**

- Selecione os locais de trabalho, empregadores ou grupos dos colaboradores que deseja incluir na geração do relatório.

**3.2.Seção: Por mês / Por período**

- Defina a abrangência temporal do relatório:
  - **Por mês:** Escolha um mês e ano específicos para gerar o relatório.
  - **Por período**: Defina manualmente as datas de início e fim do período desejado.

**3.3.Seção: Opções Extras**

- Opções adicionais que podem ser consideradas ou não na geração do relatório:
  - **Não considerar empregados demitidos:** Exclui do relatório colaboradores que já tenham sido desligados no período selecionado ou anteriormente.
  - **Não considerar empregados sem pontos no mês:** Remove do relatório colaboradores que não possuem registros de ponto no mês ou período escolhido.
  - **Gerar resultado em um arquivo:** Compacta o relatório em um único arquivo PDF contendo os dados de todos os colaboradores.
  - **Um arquivo por empregado:** Gera um arquivo PDF individual para cada colaborador incluído no relatório.
    - **Obs.**: Caso nenhuma das duas opções anteriores sejam selecionadas, o relatório será gerado como um arquivo PDF para cada local de trabalho.
  - **Não gerar relatório de entrega:** Desativa a geração do relatório de entrega, que é utilizado para registrar e controlar os espelhos já entregues aos colaboradores, bem como os que foram assinados.
  - **Anexar atestados na folha:** Adiciona os atestados cadastrados como anexos nos relatórios dos colaboradores correspondentes.
  - **Mostrar banco de horas:** Inclui os saldos de banco de horas (mensal e acumulado) no relatório final.
  - **Mostrar em Observações as notas adicionadas:** Exibe as notas adicionadas no sistema relacionadas aos colaboradores, diretamente no campo "Observações" do relatório.
  - **Incluir certificado de assinaturas eletrônicas no PDF:** O espelho de ponto será gerado com um certificado que comprova as assinaturas eletrônicas realizadas, garantindo mais segurança e validade jurídica ao documento.
  - **Ocultar saldos de banco de horas zerados no acumulado**: Remove do relatório as categorias de banco de horas que não possuem saldo, exibindo apenas aquelas com valores diferentes de zero. Se todos os saldos estiverem zerados, a seção de banco de horas não aparecerá no documento.
  - **Enviar os resultados do relatório por email:** ao marcar essa opção, o sistema envia automaticamente o espelho de ponto gerado para o e-mail do usuário, facilitando o compartilhamento e armazenamento do documento.

**3.4.Seção: Omitir Campos**

- Nesta seção, você pode personalizar o relatório omitindo informações específicas que não são relevantes para o objetivo da análise ou entrega. Confira o significado de cada opção:
  - **Admissão**: Exclui do relatório a data de admissão dos colaboradores, caso essa informação não seja necessária.
  - **RG**: Remove o número do RG dos colaboradores do relatório.
  - **Local**: Omitirá o local de trabalho associado ao colaborador, útil quando essa informação não precisa constar no relatório final.
  - **CPF**: Exclui o CPF dos colaboradores, garantindo mais discrição caso o relatório seja compartilhado.
  - **Departamento**: Remove a informação do departamento ao qual o colaborador está vinculado.

**3.5.Seção: Agrupar por / Ordenar por**

- **Agrupar por**: Define como os dados serão organizados no relatório:

  - **Local**: Agrupa os espelhos de ponto por local de trabalho, organizando os colaboradores de cada local em um mesmo agrupamento no relatório.
  - **Empregador**: Agrupa os espelhos de ponto por empregador, facilitando a análise por organização ou unidade empresarial.
- **Ordenar por**: Define a ordem de exibição dos colaboradores dentro de cada agrupamento escolhido:

  - **Nome**: Organiza os colaboradores em ordem alfabética, permitindo uma busca mais simples por nome.
  - **Código**: Organiza os colaboradores pelo número do código do seu cadastro de empregado, em ordem crescente.

---

## Como fazer o download do Relatório

Após clicar em "gerar excel", a plataforma processará o relatório em segundo plano:

1. Clique no **ícone de sino** (Notificações), no canto inferior esquerdo da sua tela, para acompanhar a geração do arquivo.

   ![Imagem 2: Clique no ícone de sino (Notificações), no canto inferior esquerdo da sua tela, para acompanhar a geração do arquivo.](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_1a1jsg7.png)
2. Quando o status mudar para "100%", o seu relatório aparecerá como "Concluído".

![Imagem 3: Quando o status mudar para "100%", o seu relatório aparecerá como "Concluído".](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_u67h2o.png)

---

## Entendendo o arquivo gerado

Ao finalizar o processo de geração do relatório, será disponibilizado um arquivo compactado (.zip) que contém todos os documentos relacionados ao espelho de ponto. A seguir, detalhamos o conteúdo do arquivo gerado

1. **Espelho de Ponto em PDF**

   - Cada colaborador terá um relatório individual no formato PDF.
   - Os PDFs são organizados e agrupados de acordo com a estrutura definida nos filtros.
   - Cada espelho de ponto conta com as seguintes informações:
     - Dados do empregador
     - Dados cadastrais do empregado.
     - Competência e período
     - Pontos registrados
     - Jornada esperada
     - Apontamentos e valores
     - Observações
     - Consolidação dos apontamentos na competência
     - Saldo de banco de horas (se habilitado)
     - Informações de travamento
     - Área de assinaturas

   ![Imagem 4: Área de assinaturas](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_o292f9.png)
2. **Cerificado de Assinaturas**

   - Se habilitada a opção "Incluir certificado de assinaturas eletrônicas no PDF", é gerado um documento anexado ao espelho de ponto informações de auditoria das assinaturas eletrônicas realizadas no processo de fechamento de folha, incluindo:
     - Nome completo do usuário que realizou a assinatura
     - Data e hora da assinatura
     - CPF do usuário
     - E-mail do usuário
     - ID do usuário na plataforma
     - Meio utilizado para realizar a assinatura
     - Endereço IP utilizado
     - Data e hora de geração do relatório

   ![Imagem 5: Data e hora de geração do relatório](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/imageq794cl_1slewv0.png)

> ⚠️ Atenção: Ao habilitar o Certificado de Assinaturas, os campos de assinatura física ficarão ocultados no espelho de ponto.

3. **Protocolo de entrega**

   - Caso não tenha marcado a opção "não gerar relatório de entrega", será recebido também o relatório de entrega, utilizado para registrar e controlar os espelhos já entregues aos colaboradores, bem como os que foram assinados.
4. **Planilhas de Apoio**

   - Planilha de erro: Apresenta uma lista de colaboradores e as inconsistências identificadas durante o processamento, indicando os problemas que impediram a geração do relatório para o colaborador correspondente.
   - Planilha de status: Resume o status de processamento de cada colaborador incluído no relatório.

> 💡 Dicas:

- Use a planilha de erros para identificar e corrigir pendências.
- Utilize a planilha de status como um acompanhamento de quais colaboradores foram considerados na geração do relatório.
- Compartilhe os PDFs individuais com os colaboradores ou mantenha-os arquivados para auditorias e consultas futuras.
- Se precisar gerar o espelho de ponto de apenas um colaborador, confira o artigo: [R01 - Como gerar o espelho de ponto de um colaborador](https://sankhya.zendesk.com/hc/pt-br/articles/42427296190743).

---

O **relatórioR01** é uma ferramenta essencial para consolidar e analisar os registros de jornada. Com a possibilidade de personalização por filtros, opções adicionais e organização dos dados, ele oferece um controle completo e detalhado, auxiliando na identificação de pendências e nos cálculos dos apontamentos para pagamento aos colaboradores.

Caso ainda tenha dúvidas ou precise de auxílio, entre em contato com o nosso time de Suporte pelo chat integrado ao [site Gestão](https://gestao.pontotel.com.br/#/cognito/login) ou pelo [WhatsApp](https://api.whatsapp.com/send/?phone=551131852700&text&type=phone_number&app_absent=0).
