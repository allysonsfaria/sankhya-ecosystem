---
id: "44010688328471"
titulo: "Por que algumas ligações são consideradas \"encerradas\" dentro da Meetime?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010688328471-Por-que-algumas-liga%C3%A7%C3%B5es-s%C3%A3o-consideradas-encerradas-dentro-da-Meetime"
trilha: "Meetime > Dificuldade com ligações"
atualizado_em: "2026-10-05T18:44:38Z"
rotulos: ["sync_hc", "meetime", "meetime_1290", "sync_hash_613cbc7c041a"]
---

# Por que algumas ligações são consideradas "encerradas" dentro da Meetime?

Ao analisar o **painel de controle** dentro da Meetime, é possível notar que algumas ligações realizadas aparecem como “encerradas” em determinados usuários. Esse tipo de registro pode gerar dúvidas, mas está relacionado principalmente à duração da ligação.

De forma geral, consideramos nesse cenário as ligações que são finalizadas muito rapidamente após serem iniciadas, normalmente antes de 10 segundos.

## ⚠️ O que causa esse comportamento?

Esse comportamento é comum no dia a dia e pode ocorrer por alguns motivos:

- 📞 **Encerramento rápido da ligação**: quando o usuário inicia a chamada e decide desligar quase imediatamente
- 📬 **Caixa postal**: quando a ligação cai direto na caixa postal e é encerrada na sequência pelo usuário
- ⏱️ **Falta de retorno imediato:** quando não há toque perceptível ou resposta rápida, levando o usuário a encerrar a chamada antes de aguardar

![Imagem 1: ⏱️ Falta de retorno imediato: quando não há toque perceptível ou resposta rápida, levando o usuário a encerrar a…](https://ajuda.sankhya.com.br/hc/article_attachments/44010733167511)

Em todos esses casos, a ligação é finalizada antes de atingir um tempo mínimo considerado para uma tentativa efetiva de contato.

## 📊 Como essa métrica é analisada?

Um ponto importante é que essa análise acontece dentro do grupo de ligações que não foram conectadas.

Ou seja, ao olhar para todas as tentativas em que não houve conexão com o contato, parte delas pode ter sido encerrada muito rapidamente.

Por exemplo: de 10 ligações que não foram conectadas, 8 podem ter sido encerradas antes de 10 segundos representando 80% das ligações. Esse tipo de visão ajuda a entender melhor o comportamento das tentativas e traz mais contexto para operação.

## ⌛ Por que é importante aguardar alguns segundos?

Esse pequeno intervalo é essencial para que toda a estrutura da ligação seja preparada, desde a comunicação com o servidor VoIP até o roteamento da chamada.

Mesmo quando a ligação cai na caixa postal, esse tempo garante que o sistema reconheça a tentativa como uma chamada concluída e registre corretamente o status.

## 🚫 Como evitar Esses tipos de ligação?

A melhor forma de evitar esse cenário é simples e envolve apenas um ajuste de comportamento no dia a dia.

Após iniciar uma ligação, o ideal é aguardar alguns segundos antes de desligar, garantindo que a conexão seja estabelecida. Isso vale mesmo nos casos em que a chamada não é atendida.

Na prática:

- ✅ Evite encerrar a ligação imediatamente
- ✅ Aguarde cerca de 10 segundos antes de desligar
- ✅ Permita que a chamada seja efetivamente conectada

Ainda tem dúvidas? Entre em contato com a gente através do 
e-mail [suporte@meetime.com.br](mailto:suporte@meetime.com.br) ou WhatsApp através do número de telefone [(48) 3204-7590](https://wa.me/554832047590).
