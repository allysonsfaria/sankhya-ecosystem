---
id: "42774298873239"
titulo: "LU0104: A licença de uso do sistema não pôde ser validada por falha na conexão com o serviço de validação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42774298873239-LU0104-A-licen%C3%A7a-de-uso-do-sistema-n%C3%A3o-p%C3%B4de-ser-validada-por-falha-na-conex%C3%A3o-com-o-servi%C3%A7o-de-valida%C3%A7%C3%A3o"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-09-29T17:41:12Z"
rotulos: ["Produtos", "Configuração", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Erro", "Plataforma - KCS", "SAS3", "A licença de uso do sistema", "LU0104:", "LU0104"]
---

# LU0104: A licença de uso do sistema não pôde ser validada por falha na conexão com o serviço de validação

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/42774298856471) **MENSAGEM:**

LU0104: A licença de uso do sistema não pôde ser validada por falha na conexão com o serviço de validação. Por favor, comunique o administrador do sistema para que seja verificada a conexão com a internet do servidor (SAS) e possíveis bloqueios nos endereços de acesso.

Permanecendo a falha na conexão, algumas telas e recursos do sistema poderão ficar indisponíveis daqui a X dias e X horas.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/42774291656215)SOLUÇÃO:**

**Cenários de correção da falha de validação da cadeia de certificados pelo SAS3 Linux:**

- **Alternativa 1: Ativar o INITSASONLINE (Somente Cliente que NÃO usa o MGE / DELPHI)**

Ativar o parâmetro ''**INITSASONLINE''** para casos em que o cliente esteja em versões que já tenham esta possibilidade e não tenham módulos MGE (Delphi)

| **Caso o parâmetro não exista, crie-o com as seguintes configurações: Chave: "INITSASONLINE" | Descrição: Ativa a nova versão do SAS | Módulos: Configurações | Menu: Diversas | Aba: Diversas | Tipo: Lógico | Status: Ligado.** |
| --- |

![Imagem 3: Caso o parâmetro não exista, crie-o com as seguintes configurações: Chave: "INITSASONLINE" | Descrição: Ativa a nova…](https://ajuda.sankhya.com.br/hc/article_attachments/42818507385751)

 Após Criar/habilitar o parâmetro, realize o recarregamento das licenças do sistema na tela **"Administração do servidor** (Configurações » Avançado » Administração do Servidor), aba Licença e selecione a opção **Recarregar Licença**.

![Imagem 4: Após Criar/habilitar o parâmetro, realize o recarregamento das licenças do sistema na tela "Administração do servidor…](https://ajuda.sankhya.com.br/hc/article_attachments/42775117971479)

- **Alternativa 2: Utilizar uma JRE instalada no ambiente**

**(1)** Verificar se há uma JRE instalada no servidor onde roda o SAS:

- java -version

**(2)** Caso seja uma JRE mais recente que 1.7.0\_80, já poderá ser suficiente para ajustar.

**(3)** Parar o SAS

**(4)** Renomear a pasta <PASTA\_DO\_SAS>/jre para <PASTA\_DO\_SAS>/jre\_old:

- mv <PASTA\_DO\_SAS>/jre <PASTA\_DO\_SAS>/jre\_old

**(5)** Iniciar o SAS

- **Alternativa 3: Atualizar manualmente a JRE do SAS**

**(1)** Parar o SAS

**(2)** Fazer download do arquivo para a pasta do SAS:

- cd <PASTA\_DO\_SAS>
   wget https://objectstorage.sa-saopaulo-1.oraclecloud.com/n/grfetvhg7pdl/b/ti-files/o/jre1.8.tar.gz
   mv jre jre\_old
   tar -xzvf jre1.8.tar.gz

**(3)** Iniciar o SAS

- **Alternativa 4: Atualizar o SAS**

**(1)** Parar o SAS.

**(2)** Baixar o SAS do site de Downloads:

- cd /opt
   wget <LINK\_DO\_SAS>

**(3)** Renomear a pasta do SAS antigo

- mv <PASTA\_DO\_SAS> <PASTA\_DO\_SAS\_old>

**(4)** Descompactar o novo SAS

- tar -xzvf SAS\_3\_1b26\_Sankhya\_unixx64.tar.gz

**(5)** Copiar os arquivos de configuração da pasta antiga para o novo:

- cp <PASTA\_DO\_SAS\_old>/conf/sas.cfg <PASTA\_DO\_SAS>/conf/sas.cfg

**(6)** Ajustar os arquivos protstart.sh e protstop.sh, apontando para a nova pasta do SAS.

**(7)** Iniciar o SAS.

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/42774298857623)CAUSA:**

Foi feito uma migração da cadeia de certificados, sendo necessário atualização da JRE do SAS.
