---
id: "43675281585815"
titulo: "Por que os valores do FGTS apresentado no Resumo de Folha podem ser diferentes dos apresentados no FGTS Digital?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43675281585815-Por-que-os-valores-do-FGTS-apresentado-no-Resumo-de-Folha-podem-ser-diferentes-dos-apresentados-no-FGTS-Digital"
trilha: "Melhores Práticas > Pessoal+"
atualizado_em: "2026-10-03T10:36:06Z"
rotulos: ["Artigo criado KCS", "Sankhya RH - KCS"]
---

# Por que os valores do FGTS apresentado no Resumo de Folha podem ser diferentes dos apresentados no FGTS Digital?

A divergência de valores entre o **Resumo da Folha de Pagamento** e o **FGTS Digital** é uma dúvida frequente entre os usuários do ERP. Essa diferença pode ocorrer em razão de critérios distintos de apuração, parametrização dos eventos e do processamento das informações entre o sistema interno, o eSocial e o FGTS Digital.

Para realizar uma conferência adequada, é importante compreender como cada ambiente considera as informações e quais eventos compõem os valores apresentados. Dessa forma, é possível identificar se a diferença está relacionada ao cálculo realizado no sistema, à forma como os eventos foram enviados ao eSocial ou aos critérios utilizados pelo FGTS Digital para composição dos valores.

O **FGTS Digital utiliza como base as informações enviadas pelo eSocial**. Dessa forma, os valores apresentados no FGTS Digital são apurados a partir dos eventos remuneratórios e demais informações transmitidas ao eSocial, considerando as incidências de FGTS configuradas para cada rubrica.

### Principais motivos para divergências

(1)** Configuração de Eventos**

As configurações dos eventos devem ser conferidas tanto no sistema quanto no eSocial, garantindo que as **incidências de FGTS estejam compatíveis entre os dois ambientes**. Divergências nessa parametrização podem resultar em diferenças entre os valores calculados pelo sistema e os valores apurados pelo eSocial/FGTS Digital.

Para realizar essa conferência, acesse a **Tela de Eventos** (Pessoal+ » Cadastros » Eventos) e avalie os seguintes pontos:

- **Aba eSocial:** verificar a incidência de FGTS configurada para o evento. No exemplo apresentado, o evento está configurado com **FGTS = 11 – Base de cálculo do FGTS mensal**. Essa informação é enviada ao eSocial e utilizada para a apuração do FGTS. Portanto, deve ser comparada com a incidência correspondente na **Tabela de Rubricas do eSocial**, garantindo que a parametrização esteja compatível.

![Imagem 1: Aba eSocial: verificar a incidência de FGTS configurada para o evento. No exemplo apresentado, o evento está…](https://ajuda.sankhya.com.br/hc/article_attachments/43953487279895)

- **Aba Avançado:** verificar as configurações que influenciam diretamente o cálculo realizado pelo sistema. Nessa aba, deve ser avaliado o campo **Outros**, se o mesmo incide no FGTS.

![Imagem 2: Aba Avançado: verificar as configurações que influenciam diretamente o cálculo realizado pelo sistema. Nessa aba, deve…](https://ajuda.sankhya.com.br/hc/article_attachments/43953503907351)

- **Aba Bases de Cálculo:** verificar as bases vinculadas ao evento. No exemplo, o evento possui a **Base FGTS – código 1908.** Essa configuração deve ser considerada na análise, pois está relacionada à composição da base utilizada para o cálculo do FGTS para o calculo da folha.

![Imagem 3: Aba Bases de Cálculo: verificar as bases vinculadas ao evento. No exemplo, o evento possui a Base FGTS – código 1908.…](https://ajuda.sankhya.com.br/hc/article_attachments/43953503910039)

Dessa forma, a análise da configuração do evento deve considerar **a incidência de FGTS na aba eSocial, as configurações da aba Avançado e as bases vinculadas na aba Bases de Cálculo**, além da conferência da respectiva rubrica no eSocial.

Essa validação permite identificar se a divergência está relacionada à **incidência informada ao eSocial, à configuração do cálculo do evento ou à composição da base de FGTS**.

(2)** Falta de envios de eventos**

A ausência do envio dos eventos **S-1200 e/ou S-2299** pode gerar divergências na conferência dos valores, pois indica que nem todas as folhas calculadas no sistema foram transmitidas ao eSocial.

Para garantir que todas as folhas estejam liberadas e disponíveis para envio, acesse a tela **Gerenciador de Folhas** (Pessoal+ » Rotinas Folha » Gerenciador de Folhas)

Na tela, clique no ícone **“Liberação para eSocial”** e realize as seguintes configurações:

1. No campo **Tipo de Folha**, selecione **“Todas”**.
2. Informe a **Referência** que será analisada.
3. No campo **Tipo de Ação**, selecione **“Libera dados”**.
4. Selecione a **empresa e funcionários** que devem ter os dados liberados.
5. Efetue a liberação dos dados para o eSocial.

Após a liberação, acesse a **Central do eSocial** (Pessoal+ » Rotinas Folha » Central do eSocial) e realize a geração dos eventos **S-1200 e S-2299**.

Caso os eventos sejam gerados, avalie a situação apresentada para cada evento:

- **Inclusão:** indica que o evento ainda não havia sido enviado ao eSocial e será transmitido como um novo evento.
- **Alteração:** indica que já existe um evento enviado anteriormente e o sistema identificou informações que precisam ser atualizadas. Nesse caso, é possível consultar o evento para verificar quais informações estão sendo alteradas antes de realizar o envio.

Dessa forma, é possível garantir que as folhas calculadas no sistema estejam devidamente liberadas, geradas e transmitidas ao eSocial, reduzindo o risco de divergências na apuração e conferência dos valores.

### Boas práticas para evitar divergências e conferir o resumo

Para reduzir a ocorrência de divergências entre os valores apresentados no **resumo do sistema de folha** e os valores apurados no **FGTS Digital**, recomenda-se:

- **Parametrizar corretamente todas as rubricas e eventos**, principalmente aqueles que foram personalizados, garantindo que suas incidências e configurações estejam compatíveis com as regras do eSocial.
- **Realizar conferências periódicas por meio dos relatórios S-5003 e S-5013.** Esses relatórios permitem detalhar as informações por trabalhador e podem auxiliar na identificação dos funcionários que apresentam divergências, facilitando a análise e a realização dos ajustes necessários.
- **Manter o sistema atualizado**, garantindo que as regras e adequações relacionadas ao eSocial e ao FGTS sejam aplicadas corretamente, além de assegurar o adequado processamento e envio dos eventos.

Seguindo essas orientações, é possível **minimizar a ocorrência de divergências**, facilitar a identificação da origem dos valores apresentados e garantir maior consistência entre os cálculos realizados no sistema de folha, as informações transmitidas ao eSocial e os valores disponibilizados no **FGTS Digital**.
