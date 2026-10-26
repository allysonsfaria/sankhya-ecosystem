---
id: "4403266262935"
titulo: "Falta de espaço no servidor de aplicação, o que excluir? (Linux)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4403266262935-Falta-de-espa%C3%A7o-no-servidor-de-aplica%C3%A7%C3%A3o-o-que-excluir-Linux"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:23:59Z"
rotulos: ["não apagar", "#validadoJoao", "Linux", "Falta de Espaço no Servidor de Aplicação (Linux)", "Manutenção", "SankhyaOm", "Servidor de Aplicação", "TI", "Espaço em Disco"]
---

# Falta de espaço no servidor de aplicação, o que excluir? (Linux)

**![Imagem 1: ATENÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16343614550551) ATENÇÃO:**

Recomendamos que solicite a equipe de TI da Empresa que execute o procedimento abaixo, programando um horário que não irá interromper a operação da empresa, ou avisando aos usuários sobre a manutenção e que o sistema ficará fora do ar, por alguns instantes.

O servidor de aplicação geralmente tem um espaço de armazenamento limitado, e com o tempo e uso da aplicação **SankhyaOm**, este espaço vai ficando cheio até sua totalidade máxima (100%), com isso surge a dúvida: o que posso excluir nesta partição?

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16343630947351) SOLUÇÃO:**

#### Verifique o espaço em disco:

com usuário root ou mgeweb:

df -h

![Imagem 3: df -h](https://ajuda.sankhya.com.br/hc/article_attachments/4403265694743)

No exemplo acima é possível notar que a partição 'vg00-lvbarra' do tipo ext4 montado no diretório / está com 100% gerando erros ao acessar o sistema, realizar impressões, diretório inválido, entre outros.

#### Altere o usuário para mgeweb:

su -l mgeweb

\*(Dica com root não irá solicitar senha para troca de usuário)

#### Exclua pacotes de instalações antigas do Gerenciador de Pacotes:

ls

cd sankhyaW\_gerenciador\_de\_pacotes/pkgs

\*(Dica cd sankhyaW digite TAB para autocompletar)

![Imagem 4: *(Dica cd sankhyaW digite TAB para autocompletar)](https://ajuda.sankhya.com.br/hc/article_attachments/4403265869079)

ls (Para Listar os arquivos para exclusão)

![Imagem 5: ls (Para Listar os arquivos para exclusão)](https://ajuda.sankhya.com.br/hc/article_attachments/4403265888535)

#### Exclua os pacotes de instalações (pkgs) antigas:

rm jiva-w\_3.30b640.pkg sankhya-w\_3.29b507.pkg sankhya-w\_4.7b656.pkg (Enter)

ls (Para listar novamente e confirmar a exclusão)

#### A cada atualização do sistema o Wildfly cria um ponto de restauração com o mesmo tamanho do pacote de instalação, realize a exclusão e deixe somente o arquivo da última versão:

cd (retorna ao diretório raiz e permite a utilização da tela TAB para autocompletar)

cd wildfly\_producao/sk-restore-points

ls

![Imagem 6: ls](https://ajuda.sankhya.com.br/hc/article_attachments/4403273257879)

rm -rf 4.7b415/ 4.7b599/

\*(Dica para exclusão de pastas utilizamos a função **r** (recursive) e **f** (force))

ls (Para confirmar a exclusão)

#### Remova pkgs baixados pelo WPM (Web Package Manager):

cd

cd sankhyaw-wpm/pkgs/

ls

![Imagem 7: ls](https://ajuda.sankhya.com.br/hc/article_attachments/4403266072983)

rm sankhya-w\_4.7b656.pkg

\*(Dica verifique também se não existe a pasta wildfly\_producao/sankhyaw-wpm/pkgs e realize o mesmo procedimento de exclusão)

#### Pare a aplicação e remova as pastas temporárias:

ps -ef | grep wildfly\_producao

kill -9 [numero serviço]

seta para cima para voltar o comando:

ps -ef | grep wildfly\_producao

e conferir e o sistema está parado:

![Imagem 8: e conferir e o sistema está parado:](https://ajuda.sankhya.com.br/hc/article_attachments/4403266092823)

Acesse o diretório para exclusão das pastas temporárias:

cd wildfly\_producao/standalone

ls

rm -rf log/ sysmon/ tmp/

![Imagem 9: rm -rf log/ sysmon/ tmp/](https://ajuda.sankhya.com.br/hc/article_attachments/4403273325463)

#### Inicie o sistema novamente e verifique o espaço que foi liberado:

cd

Opção 1:

jb\_startprod (caso não tenha o aliás criado iniciar utilizar a segunda opção)

**Opção 2:**

nohup /home/mgeweb/wildfly\_producao/bin/standalone.sh -bmanagement 0.0.0.0 >& /dev/null &

#### Verificando o espaço liberado no procedimento:

df -h

![Imagem 10: df -h](https://ajuda.sankhya.com.br/hc/article_attachments/4403266181015)

Neste exemplo nossa partição / que estava com 100% ficou agora com 86% e com 4,7gb livres.

**![Imagem 11: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16343630949783) OBSERVAÇÃO:**

Este procedimento é geralmente executado pela Equipe de TI da Empresa, que possui permissões de **ADMINISTRADOR.**

**![Imagem 12: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16343614560151)CAUSA:**

Mensagem apresentada devido à partição do HD em que o **SankhyaOm** está instalado ter chegado a 100% de ocupação.
