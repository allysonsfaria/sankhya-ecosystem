---
id: "5428090623511"
titulo: "Portaria Conjunta SEPRT/RFB nº 82"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/5428090623511-Portaria-Conjunta-SEPRT-RFB-n%C2%BA-82"
trilha: "Dúvidas Frequentes > Pessoal+"
atualizado_em: "2026-07-29T13:30:10Z"
rotulos: ["Configuração", "FAP", "Atualização", "Impostos", "#validadoRayssa", "eSocial", "Atualização da Portaria Conjunta SEPRT/RFB nº 82"]
---

# Portaria Conjunta SEPRT/RFB nº 82

Conforme publicado na Portaria Conjunta SEPRT/RFB nº 82, foi aprovado o leiaute final do eSocial Simplificado, versão S-1.0. O eSocial Simplificado foi previsto na Lei nº 13.874/19 e entrará em operação a partir do dia 22/05/2022.

Houve redução em mais de 30% do número de campos dos leiautes do eSocial, o que inclui a simplificação de vários eventos e a exclusão total de 13 eventos transmitidos pelas empresas, eliminando as duplicidades e redundâncias existentes.

Precisamos de um ponto de atenção nos eventos abaixo que sofreram alterações nas regras da versão 2.5 para 1.0 da simplificação. Ao fazer a virada para a versão do e-Social simplificado os eventos vão ser gerados com alteração considerando a nova regra que se aplica.

#### Evento S-1005: Tabela de Estabelecimentos, Obras ou Unidades de Órgãos Públicos

Alterado a regra de envio da tag´s:

Alíquota RAT e FAP’ (Cadastro da empresa) passa a ser enviado somente se existir um processo vinculado, diante disso os eventos vão ser gerados após virada para a versão 1.0 como alteração.

**Observação:** inclua a validade considerando a referência atual

#### Evento S-2200: Cadastramento Inicial do Vínculo e Admissão

####

#### Evento S-2206: Alteração de Contrato de Trabalho

Para as tag’s abaixo o sistema irá gerar alterações considerando as novas regras:

**(1)**DTOPCFGTS (Cadastro do funcionário) enviado somente para funcionários com categoria 104 e 106.

**(1)**DSCTPJORN’ (Cadastro da carga horária) passa a ser enviada a descrição de todas as cargas horárias.

Para as tag’s abaixo **realize as configurações** dos campos:

**(1)**TPJORNADA (Cadastro da carga horária)  passa a ser enviada a o tipo de jornada configurado no cadastro cargas horárias.

**(1)** HRNOTURNO (Cadastro da carga horária) passa a ser enviado o indicativo da  jornada semanal se possui horário noturno.

Salientamos então que as alterações relacionadas às novas regras são **legítimas e podem ser enviadas,** já que nas configurações  da nova versão elas são plausíveis. Demais tag’s incluídas serão levadas no momento que acontecer uma alteração que impactam no envio do respectivo evento.

Para mais informações, acesse o artigo: [ESocial simplificado - Orientações de atualização](https://ajuda.sankhya.com.br/hc/pt-br/articles/5242850702231)
