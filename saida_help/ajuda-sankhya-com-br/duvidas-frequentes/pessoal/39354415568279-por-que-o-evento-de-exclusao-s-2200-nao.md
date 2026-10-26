---
id: "39354415568279"
titulo: "Por que o evento de exclusão S-2200 não é gerado ao marcar \"Não sujeito a admissão no eSocial\"?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39354415568279-Por-que-o-evento-de-exclus%C3%A3o-S-2200-n%C3%A3o-%C3%A9-gerado-ao-marcar-N%C3%A3o-sujeito-a-admiss%C3%A3o-no-eSocial"
trilha: "Dúvidas Frequentes > Pessoal+"
atualizado_em: "2026-08-27T18:26:23Z"
rotulos: ["Folha", "eSocial", "Configuração Funcionários", "Central do eSocial", "Erro", "S-2200", "Artigo criado KCS", "Sankhya RH - KCS"]
---

# Por que o evento de exclusão S-2200 não é gerado ao marcar "Não sujeito a admissão no eSocial"?

Ao marcar o campo **"Situação no eSocial"** como **"Não sujeito a admissão no eSocial"** no cadastro do funcionário, o sistema pode não gerar automaticamente o evento de exclusão S-2200.

Para que o processo de exclusão funcione adequadamente, é fundamental seguir o procedimento correto dentro da **"Central do eSocial"** (Pessoal+ » Rotinas Folha » Central do eSocial), evitando realizar exclusões manuais diretamente no portal do governo.

### Procedimento correto para gerar a exclusão do S-2200

Para gerar corretamente o evento de exclusão S-2200, siga o procedimento abaixo:

**(1)** Acesse a **"Central do eSocial"** (eSocial Central eSocial).
**(2)** Clique na aba **"Recibos"**.
**(3)** Selecione a opção **"Recibos por Evento"**.
**(4)** Escolha o evento **"S-2200"** na lista de eventos.
**(5)** Localize o evento do funcionário desejado na listagem.
**(6)** Clique no ícone de **"Lixeira"** ao lado direito do evento para excluí-lo.
**(7)** Acesse a aba **"Eventos Pendentes"**.
**(8)** Selecione o evento **"S-2200"** na lista de eventos pendentes.
**(9)** Verifique que o evento de exclusão está disponível para envio e proceda com o envio ao eSocial.

### Erro ao excluir evento com dependências

Caso o sistema apresente o **"Erro 675"** ao tentar excluir o evento S-2200, isso indica que existem outros eventos trabalhistas vinculados ao mesmo contrato do funcionário, como o **"S-2220"** (Monitoramento de Saúde do Trabalhador) ou outros eventos, exceto o **"S-2190"**.

Nesta situação, exclua primeiro os eventos dependentes antes de excluir o **"S-2200"**. Por exemplo, se houver um evento **"S-2220"** registrado, exclua-o primeiro seguindo o mesmo procedimento descrito acima, e somente depois proceda com a exclusão do evento principal.

### Evite exclusões manuais no portal do eSocial

Realizar a exclusão manual do evento diretamente no portal do eSocial do governo é um processo inadequado que pode gerar inconsistências entre o sistema e a base de dados do eSocial. Quando a exclusão é feita manualmente no portal, o sistema não consegue sincronizar corretamente as informações, impedindo a geração adequada do evento de exclusão.

Utilize sempre o procedimento correto dentro da **"Central do eSocial"** para garantir que todas as informações sejam processadas adequadamente e que não ocorram erros de sincronização ou ausência de informações necessárias para o envio dos eventos.
