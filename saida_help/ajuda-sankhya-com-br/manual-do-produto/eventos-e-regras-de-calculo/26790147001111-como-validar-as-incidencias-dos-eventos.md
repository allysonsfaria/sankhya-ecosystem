---
id: "26790147001111"
titulo: "Como validar as incidências dos eventos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26790147001111-Como-validar-as-incid%C3%AAncias-dos-eventos"
trilha: "Manual do Produto > Pessoas+ > Configurações e Cadastros > Eventos e Regras de Cálculo"
atualizado_em: "2026-10-07T15:39:36Z"
rotulos: ["Configuração", "Eventos", "Impostos", "eSocial", "Central do eSocial"]
---

# Como validar as incidências dos eventos

```
 Versão disponível: A partir da 5.19
```

Esta jornada visa garantir a confiabilidade das informações dos eventos que são padrão Sankhya e auxiliar na criação de [Eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405026143767) personalizados assegurando que as configurações para o cálculo e para o eSocial estejam compatíveis, evitando diferenças na apuração dos impostos no fechamento da folha de pagamento.

### Imagem 1: Bloqueio de edição de incidências nos eventos padrões Bloqueio de edição de incidências nos eventos padrões

Para os eventos padrões da Sankhya, não será possível realizar alteração na configuração das incidências de impostos presentes na tela Eventos, na aba [Avançado](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405026143767-Eventos#AbaAvan%C3%A7ado), sendo elas: **"Base DIRF"**, **"Base SEFIP"**, **"FGTS"**, **"IRRF"**, **"Baese GRRF"** e **"INSS"**.

![Imagem 2: Para os eventos padrões da Sankhya, não será possível realizar alteração na configuração das incidências de impostos…](https://ajuda.sankhya.com.br/hc/article_attachments/26818594333591)

### Imagem 3: Bloqueio de edição de bases de cálculo nos eventos padrões Bloqueio de edição de bases de cálculo nos eventos padrões

Quando se tratar de Eventos padrões, também não poderá excluir as [Bases de cálculo](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405026143767-Eventos#ababasesdecalculo) cadastradas e que  também são padrão Sankhya.

![Imagem 4: Quando se tratar de Eventos padrões, também não poderá excluir as Bases de cálculo cadastradas e que também são padrão…](https://ajuda.sankhya.com.br/hc/article_attachments/26817807797399)

**Nota:** as Bases de cálculo personalizadas poderão ser incluídas ou excluídas normalmente.

### Imagem 5: Validação de configurações de incidência ao criar um novo Evento Validação de configurações de incidência ao criar um novo Evento

Quando se tratar de um novo Evento personalizado, ao realizar o cadastro e clicar no botão Confirmar alterações serão feitas as validações entre as incidências de impostos para os cálculos, as bases de cálculo vinculadas e as incidências de impostos para o eSocial. Caso haja alguma inconsistência, será apresentada uma mensagem informando qual é a divergência para que seja sanada e finalizado o cadastro desse Evento.

![Imagem 6: Quando se tratar de um novo Evento personalizado, ao realizar o cadastro e clicar no botão Confirmar alterações serão…](https://ajuda.sankhya.com.br/hc/article_attachments/26818534586263)

### Imagem 7: Pop up com auditoria de eventos na tela Cálculos Pop up com auditoria de eventos na tela Cálculos

Para realização dos cálculos, o sistema faz as seguintes validações:

- Comparação das incidências para o cálculo com as incidências para eSocial e o contrário também;
- Comparação entre as incidências para o cálculo e as bases de cálculo cadastradas e vice-versa.

Desse modo, ao abrir a tela [Cálculos](https://ajuda.sankhya.com.br/hc/pt-br/articles/20441795691031), caso haja inconsistências cadastrais nos Eventos, será apresentado um pop-up que exibirá o(s) evento(s) configurado(s) incorretamente e qual a divergência que deverá ser corrigida.

![Imagem 8: Desse modo, ao abrir a tela Cálculos , caso haja inconsistências cadastrais nos Eventos , será apresentado um pop-up…](https://ajuda.sankhya.com.br/hc/article_attachments/26817896940695)

Nesse caso, ao clicar em **"Continuar Cálculo"**, poderá dar andamento ao cálculo e posteriormente realizar essas correções.

Já, se clicar no botão **"Corrigir Divergências"** será direcionado à tela [Eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405026143767) para realizar imediatamente as devidas correções ou poderá clicar diretamente sobre o Evento listado, assim, também será direcionado à tela Eventos, posicionado no cadastro do referido Evento.

Tem-se ainda, a opção de **"Exportar para Planilha"** em Excel com todas as divergências apresentadas, assim, poderá visualizá-las de forma mais clara para realizar as correções.

Após tratar as divergências, pode-se realizar o cálculo com segurança.
