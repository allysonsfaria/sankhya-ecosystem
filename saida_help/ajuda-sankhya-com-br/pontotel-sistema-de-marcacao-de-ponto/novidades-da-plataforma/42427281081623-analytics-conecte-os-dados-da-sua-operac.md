---
id: "42427281081623"
titulo: "Analytics: conecte os dados da sua operação às ferramentas de BI e crie análises personalizadas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427281081623-Analytics-conecte-os-dados-da-sua-opera%C3%A7%C3%A3o-%C3%A0s-ferramentas-de-BI-e-crie-an%C3%A1lises-personalizadas"
trilha: "PONTOTEL: Sistema de marcação de ponto > Novidades da plataforma"
atualizado_em: "2026-08-03T13:29:53Z"
rotulos: ["sync_hc", "pontotel", "pontotel_6a3328550971f31bce8f8b2b", "sync_hash_f5db2ee9bf0f"]
---

# Analytics: conecte os dados da sua operação às ferramentas de BI e crie análises personalizadas

Empresas que utilizam dados para tomar decisões estratégicas sabem o quanto pode ser desafiador consolidar informações vindas de diferentes sistemas.
Muitas vezes, equipes de RH, Departamento Pessoal, Tecnologia e BI precisam exportar planilhas manualmente para cruzar informações de jornada, horas extras, absenteísmo, turnover, produtividade e indicadores de jornada. Além de consumir tempo, esse processo aumenta o risco de inconsistências e dificulta análises mais avançadas.
Para eliminar esse gargalo, a Pontotel oferece o **Analytics**, um serviço que disponibiliza acesso estruturado aos dados da plataforma para que sua empresa possa integrá-los ao ecossistema de dados já utilizado internamente.

Neste artigo, você entenderá como o Analytics funciona, quais informações estão disponíveis para análise e como a solução pode apoiar estratégias orientadas por dados.

---

## O que é o Analytics?

O Analytics é um **serviço complementar** da Pontotel que disponibiliza acesso seguro aos dados da plataforma por meio de um banco de dados relacional estruturado.
A solução foi desenvolvida para empresas que desejam criar dashboards personalizados, desenvolver análises avançadas ou integrar os dados da gestão de jornada com outras fontes de informação utilizadas no negócio.
Diferentemente do [Farol do DP](https://sankhya.zendesk.com/hc/pt-br/articles/42427250138903), que oferece dashboards prontos diretamente dentro da plataforma Pontotel, o Analytics fornece acesso aos dados para que sua empresa tenha liberdade para construir suas próprias análises.

---

## Como funciona?

A Pontotel disponibiliza um ambiente seguro contendo **views analíticas** estruturadas e documentadas.
Essas views podem ser consumidas por ferramentas de Business Intelligence, plataformas de dados, data lakes, data warehouses ou outros ambientes analíticos utilizados pela empresa.
Após a configuração da integração, sua equipe de tecnologia, BI ou parceiro especializado poderá sincronizar os dados e utilizá-los para construir dashboards, relatórios e indicadores personalizados.

---

## Principais benefícios

Ao utilizar o Analytics, sua empresa passa a contar com:

- acesso estruturado aos dados da Pontotel;
- integração com ferramentas de BI e plataformas analíticas;
- autonomia para criação de dashboards personalizados;
- cruzamento de dados com outros sistemas corporativos;
- redução da dependência de exportações manuais;
- análises mais rápidas e confiáveis;
- suporte à tomada de decisão baseada em dados;
- maior visibilidade sobre indicadores operacionais e estratégicos.

---

## Compatibilidade com ferramentas de BI

O Analytics não está limitado a uma ferramenta específica.
Os dados podem ser consumidos por diversas soluções de mercado, como:

- Power BI;
- Tableau;
- Looker Studio;
- Qlik Sense;
- Metabase;
- Apache Superset;
- Data Lakes;
- Data Warehouses;
- outras plataformas compatíveis com a estratégia de dados da sua empresa.

---

## Quais informações estão disponíveis para integração?

O Analytics disponibiliza um conjunto de views especializadas para consulta e análise.

### Dados cadastrais e estrutura organizacional

Permite consultar informações relacionadas aos colaboradores e à estrutura da empresa.
Dados disponíveis:

- identificação do colaborador;
- código interno;
- CPF ou documento equivalente;
- data de admissão;
- data de desligamento;
- cargo;
- departamento;
- empregador;
- local de trabalho;
- liderança direta;
- e-mail de acesso.

### Jornada diária

Disponibiliza uma visão consolidada da jornada de cada colaborador.
Informações disponíveis:

- dias trabalhados;
- férias;
- afastamentos;
- feriados;
- justificativas;
- presença obrigatória;
- horários registrados;
- duração da jornada.

### Marcações de ponto

Disponibiliza informações detalhadas sobre cada registro de ponto realizado.
Entre os dados disponíveis estão:

- horários registrados;
- entradas, pausas, retornos e saídas;
- origem da marcação;
- tipo de coletor utilizado;
- tipo de REP;
- registros online e offline;
- status de processamento;
- endereço IP;
- fuso horário;
- geolocalização;
- precisão da localização;
- QR Code;
- métodos de identificação utilizados.

### Recursos avançados de auditoria

Além das informações tradicionais de ponto, o Analytics disponibiliza dados que podem apoiar auditorias e controles internos.
Entre eles:

- resultado do reconhecimento facial;
- validação biométrica;
- detecção de vivacidade (liveness);
- tentativas de manipulação de localização (location spoofing);
- status do horário automático do dispositivo;
- status do fuso horário automático;
- hash de validação;
- CRC16 para integridade dos registros.
  Essas informações permitem criar dashboards e alertas personalizados para monitoramento de conformidade e segurança operacional.

### Banco de horas

Permite acompanhar toda a movimentação relacionada ao banco de horas.
Informações disponíveis:

- créditos;
- débitos;
- saldos acumulados;
- vencimentos;
- histórico diário;
- histórico mensal;
- baixas realizadas;
- pagamentos relacionados ao banco de horas.

### Dispensas e absenteísmo

Permite analisar ausências e justificativas registradas na plataforma.
Informações disponíveis:

- motivo da dispensa;
- períodos de ausência;
- colaborador;
- equipe;
- empregador;
- local de trabalho.

### Férias

Disponibiliza dados relacionados ao planejamento e às solicitações de férias.
Informações disponíveis:

- períodos de férias;
- aprovações;
- venda de férias;
- adiantamento de décimo terceiro;
- histórico de solicitações.

### Gestão de horas extras

Permite acompanhar todo o fluxo de aprovação das solicitações de horas extras.
Informações disponíveis:

- solicitações;
- aprovações;
- recusas;
- justificativas;
- aprovadores;
- períodos planejados;
- duração das horas extras.

### Turnover

Disponibiliza indicadores consolidados relacionados à movimentação de colaboradores.
Informações disponíveis:

- admissões;
- desligamentos;
- taxa de turnover;
- colaboradores ativos;
- movimentação total;
- retenção em 6 meses;
- retenção em 12 meses.

---

## Exemplos de análises que podem ser criadas

Com o Analytics, sua empresa pode desenvolver dashboards personalizados para:

- custos com horas extras;
- banco de horas por unidade;
- absenteísmo por equipe;
- turnover por departamento;
- indicadores de presença;
- auditoria de marcações;
- conformidade trabalhista;
- produtividade operacional;
- indicadores de retenção;
- acompanhamento de férias;
- custos de mão de obra;
- dashboards executivos para diretoria.
  Além disso, os dados da Pontotel podem ser cruzados com informações de outros sistemas da empresa, como ERPs, CRMs, plataformas financeiras, sistemas logísticos ou ferramentas de gestão.

---

## Analytics ou Farol do DP?

Embora sejam complementares, as soluções possuem objetivos diferentes.

### Farol do DP

Ideal para empresas que desejam acompanhar indicadores prontos diretamente dentro da Pontotel.

Características:

- dashboards prontos;
- implementação rápida;
- indicadores desenvolvidos por especialistas da Pontotel;
- foco em acompanhamento operacional.
  Saiba mais sobre o Farol do DP no artigo: [Farol do DP: acompanhe indicadores da jornada de trabalho em tempo real](https://sankhya.zendesk.com/hc/pt-br/articles/42427250138903)

### Analytics

Ideal para empresas que desejam criar análises próprias e integrar dados ao seu ecossistema corporativo.

Características:

- acesso estruturado aos dados;
- dashboards totalmente personalizados;
- integração com ferramentas de BI;
- liberdade para cruzamento de informações;
- foco em análises avançadas e estratégicas.

---

## Perguntas frequentes

### O Analytics substitui o Farol do DP?

Não.
O Farol do DP oferece dashboards prontos para acompanhamento operacional. O Analytics disponibiliza acesso aos dados para que sua empresa desenvolva análises personalizadas.
As soluções podem ser utilizadas de forma complementar.

### O Analytics fornece dashboards prontos?

Não.
O serviço disponibiliza acesso aos dados estruturados. A construção dos dashboards é realizada pela própria empresa ou por seus parceiros de tecnologia e BI.

### Posso utilizar qualquer ferramenta de BI?

Sim.
O Analytics foi desenvolvido para permitir a integração com diferentes ferramentas de Business Intelligence e plataformas analíticas.

### Posso cruzar os dados da Pontotel com outros sistemas?

Sim.
Essa é uma das principais vantagens da solução. Os dados podem ser combinados com informações provenientes de ERPs, CRMs, sistemas financeiros, plataformas logísticas e outras fontes utilizadas pela empresa.

### Posso alterar dados da Pontotel através do Analytics?

Não.
O acesso disponibilizado é exclusivamente para consulta e análise dos dados.
Toda manutenção operacional continua sendo realizada pelos ambientes oficiais da Pontotel.

### É possível criar auditorias de fraude utilizando os dados?

Sim.
As informações disponibilizadas incluem indicadores relacionados à geolocalização, biometria facial e validações de segurança que podem ser utilizadas para criação de alertas e dashboards de auditoria.

---

## Quer conhecer o Analytics na prática?

O Analytics é a solução ideal para empresas que desejam transformar os dados da jornada de trabalho em uma fonte estratégica de informação para toda a organização.
Se você deseja entender como integrar os dados da Pontotel ao seu ambiente de BI e explorar novas possibilidades de análise, agende uma apresentação sem compromisso com nossos especialistas.
🔗 [Apresentação - Analytics](https://zcal.co/i/0A20jXfP)

Para mais orientações, acesse nossa [Central de Ajuda](https://sankhya.zendesk.com/hc/pt-br) ou entre em contato com nosso time de Suporte pelo chat integrado ao site Gestão ou pelo [Whatsapp](https://api.whatsapp.com/send/?phone=551131852700&text&type=phone_number&app_absent=0).
