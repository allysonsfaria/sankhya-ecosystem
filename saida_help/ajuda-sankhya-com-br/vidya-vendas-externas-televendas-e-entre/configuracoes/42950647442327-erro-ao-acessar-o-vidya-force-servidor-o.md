---
id: "42950647442327"
titulo: "Erro ao Acessar o Vidya Force: \"Servidor ou Porta não Encontrado\""
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42950647442327-Erro-ao-Acessar-o-Vidya-Force-Servidor-ou-Porta-n%C3%A3o-Encontrado"
trilha: "VIDYA: Vendas externas, televendas e entregas > Central de ajuda > Configurações"
atualizado_em: "2026-08-24T16:07:33Z"
rotulos: ["sync_hc", "vidya", "vidya_593579", "sync_hash_6dd3ce8ad906"]
---

# Erro ao Acessar o Vidya Force: "Servidor ou Porta não Encontrado"

📌 **Sintoma do Erro**
Ao tentar acessar o link de login do Vidya Force através de navegadores web (Chrome, Edge ou similares), o usuário é barrado por uma tela de erro que impede o carregamento do sistema e a digitação de suas credenciais.

👀 **O que você vê nas Interfaces**

| **Ambiente / Módulo** | **Elementos e Alertas Exibidos na Tela** |
| --- | --- |
| **Tela do Navegador** | Mensagens explícitas de erro de rede, tais como: "servidor ou porta não encontrado", "este site não pode ser acessado" ou "ERR\_CONNECTION\_REFUSED". |

🕵️‍♂️ **Causas Mais Comuns**

- **Navegador força HTTPS:** O Chrome e o Edge possuem diretrizes nativas de segurança que tentam converter links HTTP para HTTPS de forma automática, o que quebra o acesso à rota padrão do sistema.
- **Cache Corrompido:** Informações temporárias antigas gravadas no navegador fazem com que ele insista em tentar carregar o endereço pelo caminho incorreto.
- **Bloqueio de Infraestrutura:** Firewalls corporativos ou antivírus locais configurados na rede do cliente que bloqueiam o tráfego de dados via HTTP comum.
- **Erro de Digitação:** Ausência do termo "http://" ou grafia incorreta da URL na barra de endereços.

🛠️ **Como Corrigir o Problema**

1. **Auditoria de URL:** Certifique-se de que o link digitado é exatamente `[http://app.force.vidyacode.com.br/force/login](http://app.force.vidyacode.com.br/force/login)` (utilizando **http**, sem o "s").
2. **Desativar Trava de HTTPS:** Se o navegador alterar o link para https automaticamente, clique no ícone de cadeado/informação ao lado da URL, vá em "Configurações do site" (ou "Permissões"), localize a opção "Conteúdo não seguro" e altere para **Permitir**. Em seguida, recarregue a página.
3. **Higienização do Navegador:** Pressione **Ctrl + Shift + Del**, marque a caixa "Imagens e arquivos em cache", clique em "Limpar dados" e tente o acesso novamente.
4. **Rota de Contingência:** Caso o navegador siga bloqueando, tente o acesso por uma guia anônima, utilize outro navegador (como o Firefox) ou acione o link alternativo seguro: `[https://ssl-force.vidyacode.com.br/force/vendas](https://ssl-force.vidyacode.com.br/force/vendas)`.

💡 **Quando abrir chamado para a VidyaCode**

- Se o erro de conectividade persistir mesmo após aplicar as limpezas e configurações em mais de um navegador diferente.
- Se a tela mudar de comportamento mas exibir códigos de erro internos do servidor (ex: Erro 500) ou uma tela totalmente branca.
- Se o problema não for isolado e derrubar o acesso de vários colaboradores da equipe ao mesmo tempo.
