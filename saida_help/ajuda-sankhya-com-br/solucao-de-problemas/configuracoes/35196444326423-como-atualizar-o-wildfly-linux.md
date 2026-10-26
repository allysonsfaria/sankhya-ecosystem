---
id: "35196444326423"
titulo: "Como atualizar o Wildfly - Linux?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35196444326423-Como-atualizar-o-Wildfly-Linux"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:25:47Z"
rotulos: ["Configuração", "Atualização", "Linux", "Wildfly", "Sankhya ID", "atualizar o Wildfly - Linux", "DBA com conhecimento em Linux", "JDK", "Wildfly 23 é compatível com o JDK 8u421", "JDK 11", "falhas de deploy", "instabilidade em alta carga", "funcionamento do sistema", "compatibilidade do ambiente Sankhya com as últimas versões do JDK", "quedas repentinas durante o uso do sistema", "incompatibilidade com novos recursos", "indisponibilidade de correções de segurança", "segurança e a manutenção futura do ambiente", "Artigo atualizado KCS", "Plataforma - KCS"]
---

# Como atualizar o Wildfly - Linux?

##### É fundamental manter o Wildfly sempre atualizado para a versão mais recente (versão 23 mod\_03). Essa prática garante a compatibilidade do ambiente Sankhya com as últimas versões do JDK e demais componentes de infraestrutura. Além disso, a atualização traz ganhos de desempenho e estabilidade, reduzindo o risco de falhas em produção e fortalecendo a segurança da aplicação.

#####

##### IMPORTANTE: O procedimento de atualização deve ser executado exclusivamente por um DBA com conhecimento em Linux, ou pela equipe da Cloud caso o ambiente esteja hospedado em nuvem. Antes de iniciar o processo, é obrigatório validar a versão do JDK em uso. O Wildfly 23 é compatível com o JDK 8u421(preferencialmente deve-se utilizar essa) até o JDK 11, portanto, essa versão deve estar instalada e ativada no servidor para que o ambiente funcione corretamente.

#### Instalação

##### **(1)** Acesse o servidor onde o Wildfly está instalado e pare o serviço da aplicação Sankhya.

##### **(2)** Logue-se como `root` e acesse o usuário `mgeweb`.

**(3)** Crie um backup do diretório atual do Wildfly:

```
mv wildfly_producao wildfly_producao_OLD
```

![Imagem 1: (3) Crie um backup do diretório atual do Wildfly:](https://ajuda.sankhya.com.br/hc/article_attachments/38524464800151)

**(4)**  Acesse o portal de **Downloads Sankhya Wildfly** com seu Sankhya ID;

![Imagem 2: (4) Acesse o portal de Downloads Sankhya Wildfly com seu Sankhya ID;](https://ajuda.sankhya.com.br/hc/article_attachments/38524464800535)

**(5)** Faça o download do pacote correspondente ao seu banco de dados. Copie o link do arquivo e baixe via `wget` e o servidor de aplicação no caminho `/home/mgewe`:

![Imagem 3: (5) Faça o download do pacote correspondente ao seu banco de dados. Copie o link do arquivo e baixe via wget e o…](https://ajuda.sankhya.com.br/hc/article_attachments/38524491978519)

```
wget <link_copiado>
```

![Imagem 4: (5) Faça o download do pacote correspondente ao seu banco de dados. Copie o link do arquivo e baixe via wget e o…](https://ajuda.sankhya.com.br/hc/article_attachments/38524464801943)

**(6)**  Descompacte o pacote:

```
unzip Wildfly_23.0_Sankhya_mod_03_oracle.zip
```

> Caso o `unzip` não esteja disponível:

```
sudo apt update
sudo apt install unzip
```

Arquivo **wildfly\_producao** após descompactado:

![Imagem 5: Arquivo wildfly_producao após descompactado:](https://ajuda.sankhya.com.br/hc/article_attachments/38524464803351)

**(7)** Configure o servidor no **PKG (SankhyaW Package Manager)**:

- Acesse `/home/mgeweb/sankhyaW_gerenciador_de_pacotes/bin/`
- Execute:

```
./sankhyaw-package-manager
```

- **Selecione a opção 2:** Selecionar servidor
- **Selecione a opção 2:** Configurar arranjo de portas
- Escolha `wildfly_producao` (agora com Wildfly 23)

![Imagem 6: Escolha wildfly_producao (agora com Wildfly 23)](https://ajuda.sankhya.com.br/hc/article_attachments/35196423339927)![Imagem 7: Escolha wildfly_producao (agora com Wildfly 23)](https://ajuda.sankhya.com.br/hc/article_attachments/35203441806999)

##### IMPORTANTE: O Wildfly altera a porta padrão para 8080. Ajuste para a porta correta de produção (geralmente 8180).

**(8)** Copie integralmente o arquivo `standalone.conf` do ambiente anterior (`wildfly_producao_old`) e substitua o arquivo correspondente no **WildFly 23**, assegurando a preservação completa das configurações de JVM.

- Com esse procedimento, **permanecem inalterados os parâmetros de memória**, as **configurações de Garbage Collector (GC)**, as **flags de performance**, as **variáveis de ambiente** e demais argumentos previamente definidos no **WildFly** antigo.

![Imagem 8: Com esse procedimento, permanecem inalterados os parâmetros de memória , as configurações de Garbage Collector (GC) ,…](https://ajuda.sankhya.com.br/hc/article_attachments/38524491983127)

**(9)** Ajuste os dados de conexão do banco de dados conforme instruções do DBA.

![Imagem 9: (9) Ajuste os dados de conexão do banco de dados conforme instruções do DBA.](https://ajuda.sankhya.com.br/hc/article_attachments/38524491984279)

##### IMPORTANTE: Os dados acima são individuais. Verifique também a porta HTTP, a padrão é 8080, porém se for 8180, ajuste no PKG em "Configurar arranjo de portas".

#####

![Imagem 10: IMPORTANTE: Os dados acima são individuais. Verifique também a porta HTTP, a padrão é 8080, porém se for 8180, ajuste…](https://ajuda.sankhya.com.br/hc/article_attachments/38524491986199)

**(10)** No diretório `/home/mgeweb/wildfly_producao/standalone/deployments`, garanta que apenas `mge-ds.xml` e `wpm.war` estejam presentes.

- Se `mge-ds.xml` **estiver ausente, reveja a configuração no PKG;**

![Imagem 11: Se mge-ds.xml estiver ausente, reveja a configuração no PKG;](https://ajuda.sankhya.com.br/hc/article_attachments/35196444309527)

- Também é **possível alterar a memória no WPM**, aba **"configurações".**

**(11)** Inicie o servidor com o alias:

```
jb_startprod
```

**(12)** **Acesse o WPM do Sankhya, seguindo o exemplo** **de link abaixo**, e configure a memória (se necessário). 

![Imagem 12: (12) Acesse o WPM do Sankhya, seguindo o exemplo de link abaixo , e configure a memória (se necessário).](https://ajuda.sankhya.com.br/hc/article_attachments/38524464807319)

- **Senha padrão do WPM:** `tecsis` (confirmar com responsável caso seja diferente).

![Imagem 13: Senha padrão do WPM: tecsis (confirmar com responsável caso seja diferente).](https://ajuda.sankhya.com.br/hc/article_attachments/38524464808087)

**(13)** **Ajuste também os dados de conexão de banco** e salve as configurações.

![Imagem 14: (13) Ajuste também os dados de conexão de banco e salve as configurações.](https://ajuda.sankhya.com.br/hc/article_attachments/35204428375447)

**(14)** **Instale a mesma versão do sistema utilizada anteriormente ou o último release da mesma versão.**

**(15)** **Valide o funcionamento** do ambiente atualizado.

**CAUSA**

A atualização do Wildfly é necessária para manter o ambiente **compatível com as versões atuais do JDK, do Java e do próprio Sankhya**, garantindo a continuidade do suporte técnico oficial. Além disso, a atualização corrige vulnerabilidades, melhora o desempenho e a estabilidade do servidor de aplicações.

Ambientes que permanecem em versões antigas podem apresentar:

- falhas de deploy;
- quedas repentinas durante o uso do sistema;
- incompatibilidade com novos recursos;
- instabilidade em alta carga;
- indisponibilidade de correções de segurança.

A não atualização compromete tanto o funcionamento do sistema quanto a segurança e a manutenção futura do ambiente.
