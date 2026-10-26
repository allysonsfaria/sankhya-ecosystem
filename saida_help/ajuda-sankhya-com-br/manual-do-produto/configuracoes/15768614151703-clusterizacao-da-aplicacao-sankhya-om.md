---
id: "15768614151703"
titulo: "Clusterização da aplicação Sankhya Om"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/15768614151703-Clusteriza%C3%A7%C3%A3o-da-aplica%C3%A7%C3%A3o-Sankhya-Om"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:40:56Z"
rotulos: ["Configuração", "Usuários", "servidor", "Agendamento", "Integração", "Clusterização", "Nó", "cluster", "Servidores", "Implementação de Clusterização no Sankhya Om", "WildFly", "Sankhya Om", "Banco de Dados"]
---

# Clusterização da aplicação Sankhya Om

```
 Versão disponível: A partir da 4.21
```

---

Os avanços tecnológicos têm gerado um aumento na demanda por sistemas computacionais mais robustos, capazes de lidar com tarefas complexas e volumes massivos de dados. Nesse contexto, os clusters surgem como um apoio para a escalabilidade e disponibilidade da aplicação **Sankhya Om**. 

## O que é o cluster?

Em termos simples, um cluster refere-se a um grupo de computadores interconectados que trabalham em conjunto como um único sistema coeso. Esses computadores, conhecidos como nós do cluster, são organizados em uma configuração física ou lógica próxima, permitindo que eles se comuniquem e coordenem suas atividades. 

Ao combinar o poder de processamento e os recursos de vários nós, um cluster oferece um desempenho significativamente melhor do que um único computador isolado.

### Quando utilizar a Clusterização?

Para mais de 150 usuários ativos, aloque um nó dedicado para cada conjunto de 150 usuários. Nesses casos, onde múltiplos nós para usuários são necessários, utilize um nó separado exclusivamente para Jobs e Agendamentos.

Além disso, se houver um volume significativo de integrações, é altamente recomendável um nó dedicado apenas para elas.

### Benefícios da Clusterização para o Sankhya Om

(1)** Escalabilidade flexível**: com o crescimento contínuo das operações empresariais, as demandas por recursos de computação também aumentam. A clusterização permite que o **Sankhya Om** seja escalonado verticalmente, adicionando novos nós ao cluster conforme necessário. Dessa forma, é possível lidar com um aumento no processamento e operações do sistema.

(1)** Disponibilidade e tolerância a falhas:** a clusterização melhora a disponibilidade do **Sankhya Om**, viabilizando que os serviços essenciais permaneçam operacionais mesmo em caso de falha de um nó do cluster. Isso resulta em menor tempo de inatividade e maior confiabilidade do sistema, evitando perdas de dados e impacto nos processos empresariais.

## Como ativar o modo cluster no Sankhya Om

Para alcançar a arquitetura de cluster representada na imagem, é necessário seguir as seguintes etapas:

![Imagem 1: Para alcançar a arquitetura de cluster representada na imagem, é necessário seguir as seguintes etapas:](https://ajuda.sankhya.com.br/hc/article_attachments/19878298731927)

Para começar, é fundamental que o time de TI de sua empresa configure as regras de balanceamento no Proxy Reverso, alinhando-as com as demandas específicas do seu negócio.

Para assegurar o funcionamento adequado e reduzir as alterações frequentes de nós durante as sessões, é crucial adotar o modelo de IP Hash ou equivalente no Load Balancer.

As informações que devem constar no cabeçalho dessa configuração são:

![Imagem 2: As informações que devem constar no cabeçalho dessa configuração são:](https://ajuda.sankhya.com.br/hc/article_attachments/17380244483351)

O próximo passo é a ativação da funcionalidade feita por meio da propriedade **“-Dskw.cluster.nodes”** passada na inicialização do wildfly. Para fazer esta configuração, acesse a pasta do seu servidor:

- **servidor Windows:** acesse a pasta do Wildfly > bin > arquivo standalone.conf.bat
- **servidor Linux:** a pasta que deve ser alterada é a standalone.conf

Adicione a seguinte propriedade:

```
-Dskw.cluster.nodes='IP1,IP2,IP3'
```

Confira na imagem abaixo um exemplo de configuração no arquivo standalone.conf.bat:

![Imagem 3: Confira na imagem abaixo um exemplo de configuração no arquivo standalone.conf.bat:](https://ajuda.sankhya.com.br/hc/article_attachments/19878291368087)

Nesse caso, estamos configurando três nós do cluster, onde o primeiro está localizado no endereço IP "192.168.0.107", o segundo está no endereço IP "192.168.0.106", e o terceiro no IP "192.168.0.108".

Esses endereços são fornecidos como uma lista separada por vírgulas dentro do argumento **"-Dskw.cluster.nodes"**, e esse argumento deve ser declarado em todos os nós que vão compor o cluster.

É importante ressaltar que é recomendado que cada nó tenha um endereço IP distinto para garantir o funcionamento adequado do cluster.

Na configuração do modo cluster, é possível definir qual nó será responsável pela execução dos jobs que tiveram início na inicialização do servidor de aplicações, este passo é importante, pois alguns desses jobs não devem ter mais de uma instância em execução para evitar duplicidade.

Para atribuir a responsabilidade de execução de um job a um nó específico, pode-se utilizar o argumento **"-Dskw.cluster.pref.run.job"**.

Neste caso, a configuração é a seguinte:

- **No nó executor preferencial:** inclua o argumento -Dskw.cluster.pref.run.job=true;
- **Nos demais nós:** inclua o argumento -Dskw.cluster.pref.run.job=false.

Dessa forma, o nó que tiver o argumento **"-Dskw.cluster.pref.run.job=true"** será o executor preferencial dos jobs e caso este saia do modo cluster, é necessário intervir manualmente e declarar um novo executor. Se o argumento não for declarado em nenhum nó, a aplicação do **Sankhya Om** será responsável por decidir qual nó será o executor do job.

Na imagem a seguir está representado o arquivo standalone.conf.bat do terceiro nó que será o executor de jobs:

![Imagem 4: Na imagem a seguir está representado o arquivo standalone.conf.bat do terceiro nó que será o executor de jobs:](https://ajuda.sankhya.com.br/hc/article_attachments/19878291374871)

Para garantir uma comunicação eficiente entre os nós do cluster, é imprescindível conceder permissões de leitura e escrita a determinadas pastas localizadas no diretório home do usuário no qual o sistema está instalado, isso pode ser realizado utilizando o software de compartilhamento de arquivos da sua escolha, no entanto, será necessário liberar em todos os nós os diretórios configurados nos parâmetros **"Diretório base para o repositório de arquivos - FREPBASEFOLDER"** e **"Path dos modelos de impressão/e-mail (MGE Web)** **SERVDIRMOD"**, além das pastas:

- **sps-files**: essa pasta tem a finalidade de armazenar os arquivos gerados para impressão e deve ser compartilhada para evitar a requisição do arquivo por um nó que não tem acesso à pasta;
- **Imagens**: armazena as imagens incluídas no Sankhya e precisam estar compartilhadas para garantir que as imagens estejam disponíveis em todos os nós.

Também, para a comunicação entre os nós, é necessário que as portas TCP/IP: 5701, 5702 e 5703 estejam liberadas (rede interna apenas) para comunicar entre eles.

Ao reinicializar a aplicação, o cluster será formado automaticamente com base nos endereços fornecidos e os nós do cluster estarão conectados entre si, permitindo a comunicação e a colaboração entre eles.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/15768614151703-Clusteriza%C3%A7%C3%A3o-da-aplica%C3%A7%C3%A3o-Sankhya-Om#top)
