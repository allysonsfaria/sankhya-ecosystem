---
id: "34971966800151"
titulo: "Guia rápido: como preparar seu sistema para a Reforma Tributária"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/34971966800151-Guia-r%C3%A1pido-como-preparar-seu-sistema-para-a-Reforma-Tribut%C3%A1ria"
trilha: "Manual do Produto > Fiscal e Contábil > Reforma Tributária > Comece por aqui"
atualizado_em: "2026-08-26T19:12:39Z"
rotulos: ["Configuração", "Fiscal", "Impostos", "br.com.sankhya.mgeliv.cadastros.AliquotaCbs", "br.com.sankhya.mgeliv.cadastros.AliquotaIs", "br.com.sankhya.mgeliv.cadastros.AliquotaIbs", "br.com.sankhya.mgeliv.cadastros.AliquotaMonofasica", "IBS", "CBS", "IS", "Reforma Tributária"]
---

# Guia rápido: como preparar seu sistema para a Reforma Tributária

Com a aprovação da Reforma Tributária, o Sankhya Om foi atualizado para incorporar os novos tributos: **IBS** (Imposto sobre Bens e Serviços — substitui o ICMS e o ISS), **CBS** (Contribuição sobre Bens e Serviços — substitui o PIS e a COFINS) e **IS** (Imposto Seletivo — incide sobre produtos específicos).

Este guia apresenta as etapas indispensáveis para que sua empresa esteja em conformidade. O Sankhya Om conta com as ferramentas para calcular os novos impostos, mas a configuração e a revisão dos cadastros continuam sendo responsabilidade da sua equipe.

## Passo 1: comece pelo Portal da Reforma Tributária

O Sankhya Om agora conta com o [**Portal da Reforma Tributária**](https://ajuda.sankhya.com.br/hc/pt-br/articles/41261558111255-Tela-Portal-da-Reforma-Tribut%C3%A1ria), o ponto único de acesso às rotinas fiscais da transição para o IVA Dual. Ele reúne em um só lugar as ferramentas de configuração, monitoramento e alertas da Reforma, eliminando a necessidade de navegar por menus dispersos do ERP.

O portal é ativado **automaticamente** na atualização da versão compatível do Sankhya Om — não é necessária nenhuma configuração manual para acessá-lo.

**Caminho de acesso:** Menu Principal › Livros Fiscais › Cadastros › Portal da Reforma Tributária.

A partir do portal, siga as etapas abaixo utilizando os assistentes guiados:

1. **Habilite os módulos por empresa** (somente Administrador): acesse Configurações › Empresas, selecione as empresas desejadas, clique em Habilitar / Desabilitar e ative os módulos aplicáveis (Apuração CBS, Apuração IBS, DeRE, Exceção de Alíquota e Alíquota Integral). Sem essa habilitação, a empresa não aparece nas telas do módulo correspondente.
2. **Configure a Tributação Integral (IBS e CBS):** use o módulo Tributação Integral, que disponibiliza o [Assistente de Configuração da Tributação Integral IBS e CBS](https://ajuda.sankhya.com.br/hc/pt-br/articles/36231337491479-Assistente-de-Configura%C3%A7%C3%A3o-da-Tributa%C3%A7%C3%A3o-integral-IBS-e-CBS-Reforma-Tribut%C3%A1ria) para parametrizar automaticamente os novos tributos no Sankhya Om.
3. **Configure as Exceções de Alíquota:** use o módulo Exceção de Alíquota ([Assistente de Exceções IBS/CBS](https://ajuda.sankhya.com.br/hc/pt-br/articles/41605814716695-Processo-Assistente-de-Exce%C3%A7%C3%B5es-IBS-CBS)), que analisa o histórico de documentos fiscais emitidos, identifica os NCMs e NBS que precisam de atenção e sugere a classificação tributária correta com base nas tabelas oficiais.
4. **Cumpra as obrigações acessórias (DeRE):** use o módulo [DeRE — Declaração de Regimes Específicos](https://ajuda.sankhya.com.br/hc/pt-br/articles/41605230701079-Processo-DeRE-Declara%C3%A7%C3%A3o-de-Regimes-Espec%C3%ADficos) para gerar, assinar digitalmente e transmitir os eventos obrigatórios, acompanhando o status de cada envio.

**ℹ️ Nota:** O portal não substitui os menus nativos do Sankhya Om — as mesmas rotinas continuam disponíveis nos menus tradicionais. Ele também não realiza cálculo de tributos nem substitui a revisão manual dos cadastros de produtos e parceiros.

## Passo 2: ajustes complementares nos cadastros

Complemente a configuração feita pelo portal com os ajustes abaixo nas telas de cadastro, conforme o seu negócio:

- Configure as alíquotas do [IS (Imposto Seletivo)](https://ajuda.sankhya.com.br/hc/pt-br/articles/33876093578775-Al%C3%ADquota-de-IS-Cadastro-e-Manuten%C3%A7%C3%A3o-de-Al%C3%ADquotas-do-Imposto-Seletivo-Reforma-Tribut%C3%A1ria) para os produtos aplicáveis.
- Gerencie as [alíquotas monofásicas](https://ajuda.sankhya.com.br/hc/pt-br/articles/33874590545943-Al%C3%ADquotas-Monof%C3%A1sicas-IBS-CBS-Cadastro-e-Manuten%C3%A7%C3%A3o-Reforma-Tribut%C3%A1ria), se aplicável ao seu negócio. Para revisar os cadastros base, consulte também [Alíquotas IBS](https://ajuda.sankhya.com.br/hc/pt-br/articles/33820442146199-Al%C3%ADquotas-IBS-cadastro-Reforma-Tribut%C3%A1ria) e [Alíquotas CBS](https://ajuda.sankhya.com.br/hc/pt-br/articles/33822014543895-Al%C3%ADquotas-CBS-cadastro-Reforma-Tribut%C3%A1ria).
- Habilite o cálculo por Tipo de Operação (TOP): acesse o cadastro de [Tipos de Operação (TOP)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#01K56TN2K88BREGGCND4D6DBNF) e, na seção Reforma Tributária, habilite os tributos (IS, IBS e CBS) que devem ser calculados nas notas fiscais vinculadas a cada TOP.

## Passo 3: boas práticas e próximos passos

Após a configuração inicial, siga estas recomendações para garantir uma transição segura:

- **Revise os cadastros:** faça uma auditoria completa dos cadastros de produtos e parceiros antes da data de vigência.
- **Treine sua equipe:** garanta que o time fiscal e contábil compreenda os novos processos e saiba localizar as configurações no Portal da Reforma Tributária.
- **Documente as alterações:** mantenha um registro claro das alíquotas e regras configuradas para facilitar a conformidade e o histórico.
- **Consulte o guia completo:** acesse o material detalhado preparado pelos especialistas Sankhya para entender todos os detalhes da transição.

### 💡 Dica

Para aprofundar o entendimento das regras da Reforma e da usabilidade do Sankhya Om, consulte também:

- [Tela Portal da Reforma Tributária](https://ajuda.sankhya.com.br/hc/pt-br/articles/41261558111255-Tela-Portal-da-Reforma-Tribut%C3%A1ria)
- [Como a Reforma Tributária impacta a gestão fiscal das empresas?](https://ajuda.sankhya.com.br/hc/pt-br/articles/34971761894935-Como-a-Reforma-Tribut%C3%A1ria-impacta-a-gest%C3%A3o-fiscal-das-empresas)
- [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#01K1JXGT238TBWZCB5FVHRXFNB)
- [Atualizações das versões das Notas Técnicas de NF-e na tela de Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#sub-abaNotaT%C3%A9cnicaNF-e)
