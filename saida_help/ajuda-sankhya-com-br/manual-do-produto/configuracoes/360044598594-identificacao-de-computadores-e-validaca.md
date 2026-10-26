---
id: "360044598594"
titulo: "Identificação de Computadores e Validação do Java Plugin"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598594-Identifica%C3%A7%C3%A3o-de-Computadores-e-Valida%C3%A7%C3%A3o-do-Java-Plugin"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:47:48Z"
rotulos: ["Configuração", "Impressão", "Segurança", "COMPSASMGE", "EMPLICENPORUSU", "Java Plugin", "Identificação de Computadores e Validação do Java Plugin manual", "NFS-e", "Validação do Java Plugin Após Login"]
---

# Identificação de Computadores e Validação do Java Plugin

A partir da versão 3.0 a **"Identificação de Computador"** e **"Validação do Java Plugin"** serão feitas em uma segunda etapa, após o login do usuário.

Você poderá acessar o sistema, mesmo não tendo o **"Java Plugin"** instalado e rodando corretamente. Caso você não possua o Java Plugin e tente executar alguma funcionalidade no sistema que exija este plugin, como impressões ou visualização de cubo de decisão, será lançada uma mensagem de alerta, solicitando a regularização do plugin, para que a funcionalidade seja executada.

Se o sistema estiver configurado para não autorizar a entrada de computadores desconhecidos, e o Java Plugin não estiver presente em sua máquina, o login não será efetuado. Desta forma, você deverá regularizar o plugin antes de tentar entrar no sistema.

É possível desativar a validação do Java Plugin após o login, bastará desativar o parâmetro **"Manter compartilhamento de licença com o MGE? - COMPSASMGE"**.

Se você não usar o compartilhamento de licenças com o MGE, é aconselhável que esse parâmetro seja desabilitado para que o sistema tenha uma carga mais rápida, visto que o Java Plugin será validado posteriormente, se alguma funcionalidade do sistema exigir.

**Importante:** o sistema não realiza a validação do Java Plugin na tela do login do sistema, quando este é utilizado no navegador Google Chrome, pois o mesmo não possui suporte ao java.

Ao acessar o sistema, se as seguintes configurações estiverem feitas:

**I. Usuário com Computadores liberados:** Desabilitado;

**II. Java Plugin:** Desabilitado ou Desinstalado.

O sistema irá exibir a mensagem abaixo, e permitirá acesso ao sistema:

![Imagem 1: O sistema irá exibir a mensagem abaixo, e permitirá acesso ao sistema:](https://ajuda.sankhya.com.br/hc/article_attachments/8990920925975)

Ao acessar o sistema, estando o parâmetro COMPSASMGE habilitado, o sistema mostrará a mensagem abaixo:

![Imagem 2: Ao acessar o sistema, estando o parâmetro COMPSASMGE habilitado, o sistema mostrará a mensagem abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/8990924191127)

Ao entrar no sistema com o Java Plugin desabilitado, ao tentar acessar alguma funcionalidade que exija o plugin, como impressão, por exemplo, o sistema mostrará a seguinte mensagem:

**"Não foi possível iniciar o Java Plugin. Talvez ele não esteja instalado ou pode ter sido desabilitado pelo navegador.**

**Alguns navegadores solicitam confirmação para este plugin executar, portanto se esse for o caso você deve clicar em Aceitar ou Executar.**

**Baixe a versão mais recente do Java Plugin nesse link ou verifique as configurações em seu navegador."**

Ao entrar no sistema com o Java Plugin desabilitado e tentar acessar alguma funcionalidade que exija esse plugin, como por exemplo, visualização de cubo de decisão, o sistema irá exibir a seguinte mensagem:

![Imagem 3: Ao entrar no sistema com o Java Plugin desabilitado e tentar acessar alguma funcionalidade que exija esse plugin , como…](https://ajuda.sankhya.com.br/hc/article_attachments/8991728544791)

#### Licença de Uso

O sistema conta com o parâmetro **"Mostrar aviso de empresa não licenciada por usuário? - EMPLICENPORUSU"**, que ao ser ativado, caso exista algum problema com a licença de uso do sistema em relação a determinada empresa (ausência da empresa na licença de uso, por exemplo), será apresentada uma mensagem de alerta sobre este fato, apenas para usuários específicos pertencentes à empresa que não está presente na licença.
