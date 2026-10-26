---
id: "21012474338967"
titulo: "Como enviar a folha de pagamento ao eSocial"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/21012474338967-Como-enviar-a-folha-de-pagamento-ao-eSocial"
trilha: "Manual do Produto > Pessoas+ > eSocial > Eventos Periódicos e Fechamento do eSocial"
atualizado_em: "2026-10-20T18:45:12Z"
rotulos: ["Eventos", "eSocial", "br.com.sankhya.CentraleSocial", "Folha de Pagamento", "br.com.sankhya.rh.GerenciadorFolha", "Gerenciador de Folhas", "br.com.sankhya.rh.CalculoIndFolha", "Central do eSocial", "Geração de eventos", "Pessoal+"]
---

# Como enviar a folha de pagamento ao eSocial

**Módulo:** Pessoal+
**Caminho de Acesso:**Pessoal+ > Rotinas Folha > Gerenciador de Folhas

                                      Pessoal+ > Rotinas Folha > Central do eSocial
**ID da Tela:** br.com.sankhya.rh.GerenciadorFolha

                    br.com.sankhya.CentraleSocial

---

### Descrição e Usabilidade

Após realizar o cálculo e a conferência da folha de pagamento, é necessário efetuar a liberação das folhas para o eSocial e realizar a geração dos eventos na Central do eSocial.

Essa rotina é responsável por disponibilizar os dados das folhas para geração dos eventos periódicos do eSocial, como:

- S-1200 – Remuneração do Trabalhador;
- S-1210 – Pagamentos de Rendimentos do Trabalho;
- S-2299 – Desligamento;
- S-2399 – Trabalhador Sem Vínculo – Término.

A liberação é realizada por meio do botão **Liberação para eSocial**, disponível no **Gerenciador de Folhas**.

**⚠️** Após a liberação, ainda é necessário acessar a **Central do eSocial** para gerar e transmitir os eventos.

### Pré-requisitos

Antes de realizar o envio da folha para o eSocial, valide os seguintes pontos:

- folha calculada e conferida;
- eventos de rubricas enviados ao eSocial;
- dados cadastrais da empresa atualizados;
- folhas liberadas para envio;
- usuário com acesso ao Gerenciador de Folhas e à Central do eSocial.

**⚠️** Qualquer alteração realizada após a liberação da folha exigirá nova liberação e nova geração dos eventos.

### Jornada de Uso

[GIF animado: Imagem 1: Jornada de Uso](https://ajuda.sankhya.com.br/hc/article_attachments/40495811672599)

1. Acesse o Gerenciador de Folhas (Pessoal+ > Rotinas Folha);
2. Localize a folha desejada utilizando o painel de filtros;
3. Clique no botão **Liberação para eSocial**;
4. No pop-up, selecione:

   - **Tipo de Folha**;
   - **Referência**;
   - **Tipo de ação = Liberar Dados**.
5. Escolha a **Empresa** e os **Funcionários** clicando em seus respectivos cards ou marcando **Todos**;
6. Clique em **Liberar Dados para eSocial** e confirme.

   Ao confirmar a operação, o sistema exibirá um resumo da liberação realizada.

| **⚠️**  Sempre realize a liberação de todos os tipos de folhas da competência, como:   - folha mensal; - adiantamento; - férias; - rescisão; - folhas complementares.   Atente-se:   - O evento S-1200 considera todas as folhas da competência atual.   Exemplo: competência da folha: **05/2026**  Todas as folhas da competência 05/2026 serão consideradas no S-1200.   - O evento S-1210 considera as folhas cujo pagamento ocorreu na competência atual.   Exemplo: uma folha da competência 04/2026 paga em 05/2026 será enviada no S-1210 da competência 05/2026.  Por isso, é importante conferir se folhas de competências anteriores com pagamento na competência atual também foram liberadas para envio. |
| --- |

7. Após essa liberação é necessário fazer a [Geração](https://ajuda.sankhya.com.br/hc/pt-br/articles/7064222145175-Central-do-eSocial#gera%C3%A7%C3%A3o) e [Envio](https://ajuda.sankhya.com.br/hc/pt-br/articles/7064222145175-Central-do-eSocial#eventospendentes) dos eventos na [Central do eSocial](https://ajuda.sankhya.com.br/hc/pt-br/articles/7064222145175).

   ![Imagem 2: Após essa liberação é necessário fazer a Geração e Envio dos eventos na Central do eSocial .](https://ajuda.sankhya.com.br/hc/article_attachments/40495936178199)

A liberação e o envio devem respeitar a hierarquia do eSocial.

A sequência recomendada é:

1. Rubricas (S-1010);
2. Rescisões (S-2299) da competência ainda não enviada;
3. Alterações cadastrais (S-2205);
4. Alterações contratuais (S-2206);
5. Afastamentos temporários (S-2230);
6. Remuneração (S-1200);
7. Pagamentos (S-1210);
8. Trabalhadores avulsos (S-1270);
9. Informações complementares (S-1280).

Para saber mais sobre prazos e hierarquia de envio de cada evento, consulte o [Manual de Orientação do eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-3-consolidada-ate-a-no-s-1-3-07-2026.pdf).

8. Após o envio e retorno com sucesso dos eventos periódicos, finalizar a competência por meio do menu [**Finalização**](https://ajuda.sankhya.com.br/hc/pt-br/articles/7064222145175-Central-do-eSocial#finaliza%C3%A7%C3%A3o) na Central do eSocial;

   ![Imagem 3: Após o envio e retorno com sucesso dos eventos periódicos, finalizar a competência por meio do menu Finalização na…](https://ajuda.sankhya.com.br/hc/article_attachments/40496021890839)
9. Volte ao [Gerenciador de Folhas](https://ajuda.sankhya.com.br/hc/pt-br/articles/40106318532247-Gerenciador-de-Folhas#h_01KQN6106PKSHZXJST6M9STWH7) e realize o fechamento da competência.

   ![Imagem 4: Volte ao Gerenciador de Folhas e realize o fechamento da competência.](https://ajuda.sankhya.com.br/hc/article_attachments/40496011767319)

Caso existam diferenças entre os valores do Pessoal+ e os retornados pelo eSocial, utilize o relatório [Relatório S-5001 - Conferência de Contribuições sociais INSS/PIS](https://ajuda.sankhya.com.br/hc/pt-br/articles/36419467638551) para analisar as diferenças relacionadas a:

- INSS;
- FGTS;
- IRRF.

Segue abaixo as principais causas de diferenças de IRRF, INSS e FGTS:

| **CAUSA** | **SOLUÇÃO** |
| --- | --- |
| Folha de pagamento sem liberação para envio ao eSocial. | - Fazer a [liberação para envio das folhas](https://ajuda.sankhya.com.br/hc/pt-br/articles/40106318532247-Gerenciador-de-Folhas#h_01KQN3XPDJ4KAYEW7VWMBHPXCZ) no Gerenciador de Folhas; - Realizar uma nova geração e envio na Central do eSocial. |
| Alterações no cálculo após o envio para o eSocial. | - Bloquear a liberação das folhas no Gerenciador de Folhas; - Realizar uma nova geração e envio na Central do eSocial. |
| Dados cadastrais da empresa divergentes (FAP, terceiros, INSS). | - Revisar os cadastros da empresa no sistema. |
| Cadastro de rubricas com incidências enviadas ao eSocial diferente das incidências do cálculo no Pessoal+. | - Revisar o cadastro das incidências das rubricas e fazer um novo envio do S-1010 ajustando as incidências no portal. - Excluir a folha já enviada seguindo o processo abaixo:   - Fazer a reabertura da competência na Central do eSocial;   - Bloquear o envio ao eSocial da folha que tem a rubrica incorreta no Gerenciador de Folhas;   - Com a folha bloqueada, realizar a Geração na Central do eSocial (será gerado uma exclusão da folha de pagamento);   - Enviar o evento e aguardar o retorno;   - Liberar novamente a folha de pagamento no Gerenciador de Folhas;   - Gerar os eventos na Central do eSocial;   - Enviar o evento e aguardar o retorno;   - Enviar o fechamento da competência. |

| **⚠️** **Atenção**  Para reabrir uma competência já fechada, a ordem de reabertura e a necessidade de desfazer integrações já realizadas seguem regras específicas, veja o detalhamento em **Gerenciador de Folhas**, na seção sobre o botão **Reabrir Competência**.  Para excluir um lançamento de distribuição de lucros já enviado ao eSocial, bloqueie antes a folha correspondente pela opção **Liberação para eSocial** (**Bloquear Dados**), no **Gerenciador de Folhas**. |
| --- |

## Pontos de Atenção

- Alterações na folha após envio exigem retificação;
- Folhas não liberadas não serão consideradas nos eventos periódicos;
- O S-1210 considera a data de pagamento e não a competência da folha;
- O envio deve respeitar a hierarquia dos eventos do eSocial;
- Rubricas com incidências incorretas podem gerar diferenças tributárias.

## Dicas de Usabilidade

- Sempre confira todas as folhas antes da liberação;
- Libere férias, rescisões e complementares junto da folha mensal;
- Utilize a Conferência Analítica de Tributos após o envio;
- Evite alterar cálculos após a geração dos eventos;
- Revise incidências de rubricas periodicamente.

### Artigos Relacionados

- [Gerenciador de Folhas](https://ajuda.sankhya.com.br/hc/pt-br/articles/40106318532247)
- [Central do eSocial](https://ajuda.sankhya.com.br/hc/pt-br/articles/7064222145175)
