---
id: "44013142720023"
titulo: "[TMS] - Ordem de Coleta Automática"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44013142720023--TMS-Ordem-de-Coleta-Autom%C3%A1tica"
trilha: "Lincros > TMS > Expedição - TMS"
atualizado_em: "2026-10-05T19:48:27Z"
rotulos: ["sync_hc", "lincros", "lincros_13432934", "sync_hash_1aa5f87571c1"]
---

# [TMS] - Ordem de Coleta Automática

**Menu**: Expedição > Coleta > Ordem de Coleta

**Objetivo**: Como realizar o agendamento de ordem de coleta de forma automática, conforme parâmetros informados em seu cadastro

## Considerações:

- No botão Agendar da tela de listagem é possível cadastrar o agendamento para geração automática da ordem de coleta (e envio para a transportadora);
- Com base nos filtros informados, é feita a busca dos documentos para a geração da ordem de coleta;
- Após gerada é enviado um  e-mail para a transportadora com a data e horário que foi agendada e o QR code da ordem de coleta. É possível verificar posteriormente no menu Sistema > agendamento de processos, o agendamento criado;

Abaixo segue os procedimentos para realizar o agendamento da ordem de coleta de forma automática:

1. Acessar o menu: Expedição > Coleta > Ordem de Coleta;
2. Clicar no botão 'Agendar';

   ![Imagem 1: Clicar no botão 'Agendar';](https://ajuda.sankhya.com.br/hc/article_attachments/44013142886935)
3. Preencher os dados como, por exemplo: Unidade, Transportadora, Tipo de Documento, Observação, etc.;

   ![Imagem 2: Preencher os dados como, por exemplo: Unidade, Transportadora, Tipo de Documento, Observação, etc.;](https://ajuda.sankhya.com.br/hc/article_attachments/44013103525911)
4. Na parte 'Agendamento' é onde vamos informar o período que a coleta irá ocorrer;

   ![Imagem 3: Na parte 'Agendamento' é onde vamos informar o período que a coleta irá ocorrer;](https://ajuda.sankhya.com.br/hc/article_attachments/44013112171671)
5. Após criar o agendamento, basta clicar em 'Salvar';

## Para verifica o agendamento

1. Para verificar o agendamento ou remover, acessar o menu: Sistema > Agendamento de Processos;
2. Nesta tela é possível verificar todos os agendamentos, não é aconselhável editar, mas sim remover e incluir outro agendamento;

![Imagem 4: Nesta tela é possível verificar todos os agendamentos, não é aconselhável editar, mas sim remover e incluir outro…](https://ajuda.sankhya.com.br/hc/article_attachments/44013143262103)

## Critérios para geração de Ordem de Coleta automática

A Ordem de Coleta é utilizada para agrupar todas as notas que determinada transportadora irá coletar no determinado dia. Algumas empresas por possuírem alta demanda de coleta, realizando agendamentos automáticos para que seja criado as ordens agrupando todas as notas fiscais emitidas naquele período.

Para validar se a transportadora possui agendamentos automáticos de Ordem de Coleta deve-se acessar o menu Sistema > Agendamento de  Processos e nessa tela validar se há algum agendamento com a classe 'com.transpobrasil.job.OrdemColetaJob'

**Importante**: O sistema só irá vincular na ordem de coleta de forma automática, NF-es que possuam pré-conhecimento com situação igual à 'Criado'. Ou seja, se determinada NF-e possuir, por exemplo, um pré-conhecimento com situação de 'Em transporte', então, quando o processo automático for executado o sistema irá desconsiderar essa NF-e e a mesma não entrará na Ordem de Coleta. Este é um comportamento nativo do sistema, uma regra padrão.

**Obs.:** Os campos que aparecem em vermelho são de preenchimento obrigatório.

 "Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos".
