---
id: "18367435782935"
titulo: "Gerenciador de DP"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/18367435782935-Gerenciador-de-DP"
trilha: "Manual do Produto > Pessoas+ > Autoatendimento: Portal RH, App e Requisições > Requisições"
atualizado_em: "2026-10-15T14:46:42Z"
rotulos: ["Requisições", "Fórmulas", "Notificações", "eSocial", "Gerenciador de DP", "Painel de Configurações", "Gerenciador de Folhas", "Configuração Funcionários", "ID: br.com.sankhya.rh.GerenciadorDP", "Gestão de Presença", "Timeline", "Cálculos", "Central do eSocial", "Requisições e aprovações", "Registros e acompanhamento", "Navegação e funcionalidades", "Pessoal+"]
---

# Gerenciador de DP

```
 Módulo: Pessoal+ > Rotinas Folha
```

---

O **Gerenciador de DP** é uma tela gerencial destinada aos usuários que pertencem ao DP/RH. Através desta rotina é possível analisar as requisições recebidas, ver avisos de documentos que estão a vencer e direcionar-se às telas mais acessadas.

![Imagem 1: O Gerenciador de DP é uma tela gerencial destinada aos usuários que pertencem ao DP/RH. Através desta rotina é possível…](https://ajuda.sankhya.com.br/hc/article_attachments/33326207898775)

Ao acessar essa tela, têm-se os seguintes menus: 

### ![Imagem 2: Notificações](https://ajuda.sankhya.com.br/hc/article_attachments/42310368525847) Notificações

Neste menu são apresentados todos os novos recebimentos que serão exibidos na **Timeline**. Assim, cada notificação nova será representada por um numeral acima do ícone.

![Imagem 3: Neste menu são apresentados todos os novos recebimentos que serão exibidos na Timeline . Assim, cada notificação nova…](https://ajuda.sankhya.com.br/hc/article_attachments/33326207899287)

---

### Timeline

Na **Timeline** estão dispostas todas as requisições com status de **Aguardando a aprovação do DP** para análise e tomada de decisão.

![Imagem 4: Na Timeline estão dispostas todas as requisições com status de Aguardando a aprovação do DP para análise e tomada de…](https://ajuda.sankhya.com.br/hc/article_attachments/33326207900055)

Além dos filtros por tipo de requisição e por situação (todas as requisições ou somente as pendentes de DP), é possível restringir a **Timeline** por **Departamento** e por **Líder**. Assim, você localiza rapidamente as requisições de uma área ou de uma liderança específica, sem precisar percorrer a lista inteira.

Para criar um filtro:

1. Na Timeline, abra o menu de filtros e clique em **Gerenciar filtros** (ícone de engrenagem).
2. Adicione as condições desejadas:
   - **Departamento:** exibe as requisições dos colaboradores vinculados ao departamento informado.
   - **Líder:** exibe as requisições dos colaboradores que têm o líder informado como líder direto.
3. Para considerar mais de um departamento ou mais de um líder, ligue as condições com **OU** ou utilize o operador **Contido em**.
4. Para considerar departamento e líder ao mesmo tempo, ligue os dois grupos com **E** e coloque cada grupo entre parênteses.
5. Salve e aplique o filtro.

O filtro é aplicado em conjunto com os filtros de tipo de requisição e de situação que já estiverem selecionados. Os filtros salvos ficam listados abaixo da opção **Gerenciar filtros** e podem ser reutilizados. Ao desmarcar o filtro personalizado, a Timeline volta a considerar apenas os demais filtros ativos.

| **⚠️** **Atenção**  Ao combinar departamento e líder no mesmo filtro, utilize parênteses para separar cada grupo de condições. Sem os parênteses, o resultado pode incluir requisições que não atendem aos dois critérios.  Exemplo correto: **(**Departamento = Financeiro **OU** Departamento = Comercial**)** **E** **(**Líder = Ana **OU** Líder = Carlos**)**.  Nesse caso, são exibidas somente as requisições de colaboradores do Financeiro ou do Comercial que têm Ana ou Carlos como líder direto. |
| --- |

Regras do filtro:

- O filtro por **Líder** considera apenas os subordinados **diretos** do líder informado. Os colaboradores liderados por um subordinado desse líder não são exibidos.
- O departamento e o líder considerados são os que estão no **cadastro atual** do colaborador, e não os que existiam quando a requisição foi criada. Se o colaborador mudar de líder ou de departamento, a requisição passa a aparecer no filtro do novo líder ou departamento.
- Colaboradores sem líder ou sem departamento no cadastro não aparecem no filtro correspondente. Sem o filtro personalizado, as requisições deles continuam sendo exibidas normalmente.

| ℹ️ **Nota**  Se você tem acesso a mais de uma empresa, o filtro por Líder pode reunir líderes de empresas diferentes que tenham o mesmo código de colaborador. O sistema exibe um aviso nessa situação. Confira a empresa das requisições exibidas antes de tomar uma decisão. |
| --- |

| 💡 **Dica**  Se uma requisição esperada não aparecer no filtro, confira no cadastro do colaborador se o departamento e o líder estão preenchidos corretamente. |
| --- |

**Observação:** a requisição de [Admissão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360059085273-Requisi%C3%A7%C3%B5es#admissao) integrada pelo [ATS da Mindsight](https://www.sankhya.com.br/sankhya-rh/) será enviada ao candidato automaticamente e apresentará os seguintes status para acompanhamento:

- **Formulário incompleto (E-mail Não Enviado):** caso a requisição completa seja feita pelo DP;
- **Formulário incompleto (E-mail Enviado):** quando o [formulário](https://ajuda.sankhya.com.br/hc/pt-br/articles/4408648186391-Envio-da-Requisi%C3%A7%C3%A3o-de-Admiss%C3%A3o-para-o-candidato) for enviado por e-mail para que o candidato complete o preenchimento;
- **Formulário incompleto (E-mail na Fila de Envio):** caso o e-mail esteja aguardando para ser enviado ao candidato;
- **Formulário incompleto (Novato finalizou):** quando o candidato finaliza o preenchimento e encaminha para o DP concluir a admissão;
- **Aguardando a aprovação do DP (Novato finalizou):** quando o usuário de DP finaliza toda a requisição, deixando-a pronta para aprovação.

Para aprovar ou rejeitar uma requisição, basta clicar sobre o card para visualizar as informações básicas da requisição. Sendo necessário, acrescente um **"Comentário"** e acione o botão **"Confirmar"** ou **"Rejeitar"** requisição.

[GIF animado: Imagem 5: Para aprovar ou rejeitar uma requisição, basta clicar sobre o card para visualizar as informações básicas da…](https://ajuda.sankhya.com.br/hc/article_attachments/33326211846039)

Além dessas opções Confirmar e Rejeitar, ao clicar num card de uma requisição de [Admissão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360059085273-Requisi%C3%A7%C3%B5es#admissao) pendente de aprovação, também será exibida a opção **"Editar"** para caso seja necessário alterar qualquer informação na referida requisição.

Caso ainda queira visualizar todas as informações da requisição, clique no botão ![Imagem 6: Caso ainda queira visualizar todas as informações da requisição, clique no botão "Ver Requisição" , assim, a mesma será…](https://ajuda.sankhya.com.br/hc/article_attachments/18368478756759)**"Ver Requisição"**, assim, a mesma será exibida diretamente na tela [Requisições](https://ajuda.sankhya.com.br/hc/pt-br/articles/360059085273).

É possível avaliar várias requisições de uma única vez, por meio do botão ![Imagem 7: É possível avaliar várias requisições de uma única vez, por meio do botão "Aprovar requisições em lote" . Ao acioná-lo,…](https://ajuda.sankhya.com.br/hc/article_attachments/20524710942231) **"Aprovar requisições em lote"**. Ao acioná-lo, será aberto um pop-up para seleção das requisições que deseja aprovar ou rejeitar. Após selecionar, basta clicar em Confirmar ou Rejeitar requisição.

![Imagem 8: É possível avaliar várias requisições de uma única vez, por meio do botão "Aprovar requisições em lote" . Ao acioná-lo,…](https://ajuda.sankhya.com.br/hc/article_attachments/18369104296215)

---

### ![Imagem 9: Histórico](https://ajuda.sankhya.com.br/hc/article_attachments/42310368527383) Histórico

Este menu apresenta o histórico de requisições aprovadas e reprovadas para cada funcionário e permite ainda o acompanhamento em tempo real de notícias do eSocial e Ministério da Economia.

![Imagem 10: Este menu apresenta o histórico de requisições aprovadas e reprovadas para cada funcionário e permite ainda o…](https://ajuda.sankhya.com.br/hc/article_attachments/33326250219927)

---

### ![Imagem 11: Gestão de Presença](https://ajuda.sankhya.com.br/hc/article_attachments/42310371836183) Gestão de Presença

Este menu irá direcioná-lo para a tela **Gestão de Presença**, na qual se pode visualizar quem está trabalhando no dia, no intervalo, se já chegou ao trabalho ou até mesmo se está de férias. Caso tenha liderados, é possível realizar análises diversas, como, por exemplo: distribuição salarial, maior e menor salário, tempo de casa, quantidade de dependentes, estado civil, grau de escolaridade, saldo de banco de horas, entre outros.

![Imagem 12: Este menu irá direcioná-lo para a tela Gestão de Presença , na qual se pode visualizar quem está trabalhando no dia, no…](https://ajuda.sankhya.com.br/hc/article_attachments/18371454505239)

---

De forma semelhante ao menu **Gestão de Presença**, ao clicar sobre os demais serão abertas suas respectivas telas:

| ![Imagem 13: Lideranças](https://ajuda.sankhya.com.br/hc/article_attachments/42310371836823) [Lideranças](https://ajuda.sankhya.com.br/hc/pt-br/articles/15668325935383) | ![Imagem 14: Fórmulas](https://ajuda.sankhya.com.br/hc/article_attachments/42310371838743) [Fórmulas](https://ajuda.sankhya.com.br/hc/pt-br/articles/13061392411287) |
| --- | --- |
| ![Imagem 15: Acessos Pessoal Mais](https://ajuda.sankhya.com.br/hc/article_attachments/42310371839383)[Acessos Pessoal Mais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044610574) | ![Imagem 16: Cálculos](https://ajuda.sankhya.com.br/hc/article_attachments/42310371840407) [Cálculos](https://ajuda.sankhya.com.br/hc/pt-br/articles/18612838324631) |
| ![Imagem 17: Requisições](https://ajuda.sankhya.com.br/hc/article_attachments/42310368532503) [Requisições](https://ajuda.sankhya.com.br/hc/pt-br/articles/360059085273) | [Central do eSocial](https://ajuda.sankhya.com.br/hc/pt-br/articles/7064222145175) |
| ![Imagem 18: Gerenciador de Folhas](https://ajuda.sankhya.com.br/hc/article_attachments/42310368534423) [Gerenciador de Folhas](https://ajuda.sankhya.com.br/hc/pt-br/articles/4424800696599) | ![Imagem 19: Regras de Cálculo](https://ajuda.sankhya.com.br/hc/article_attachments/42310368534935) [Regras de Cálculo](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405310442007) |
| ![Imagem 20: Painel de Configurações](https://ajuda.sankhya.com.br/hc/article_attachments/42310371844631) [Painel de Configurações](https://ajuda.sankhya.com.br/hc/pt-br/articles/14999187265559) |  |

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/18367435782935-Gerenciador-de-DP#top)
