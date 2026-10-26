---
id: "360043868974"
titulo: "O que significa a sigla GC no relatório de Diagnóstico da tela Administração do Servidor?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043868974-O-que-significa-a-sigla-GC-no-relat%C3%B3rio-de-Diagn%C3%B3stico-da-tela-Administra%C3%A7%C3%A3o-do-Servidor"
trilha: "Dúvidas Frequentes > Configurações Sankhya"
atualizado_em: "2026-07-22T15:58:14Z"
rotulos: ["#RevisadoGui", "OS-1305345", "Relatórios", "Administração do Servidor", "Performance", "Significado da Sigla GC", "Java", "Garbage Collector"]
---

# O que significa a sigla GC no relatório de Diagnóstico da tela Administração do Servidor?

**(1)** O utilitário "GC" (Garbage Collector) é uma ferramenta nativa da máquina virtual Java, que de tempos em tempos coleta da memória heap os objetos que não estão sendo utilizados.
As estatísticas presentes na tela de **"Administração"**, na aba **"Relatório de Diagnóstico"**, são fornecidas pela própria VM apontando quanto tempo foi gasto do tempo total para eliminar estes objetos. Usamos um máximo de 2% como valor de referência.

**(1)** Tempos muito altos podem indicar consumo alto de memória heap, o que leva a uma maior quantidade de execuções. Ou também pode estar relacionada a uma anormalidade no ambiente, que causa problemas de performance do servidor.

**(1)** Após uma inicialização do sistema, este tempo de GC pode ser extrapolado devido a alta carga de objetos deste processo e consequentemente uso maior de hardware. Mas depois de um tempo, em condições normais este valor deve ser normalizado abaixo dos 2%.

**(1)** Podemos enumerar alguns cuidados que refletem em um melhor uso de CPU e GC, impactando na melhoria do funcionamento do sistema:

- É importante que o hardware e software estejam corretamente dimensionados para a quantidade de usuários que utilizam o sistema;
- No servidor de aplicações só devem ser executadas atividades relacionadas ao sistema;
- Observar e ajustar os Parâmetros de Performance da aba Relatório de Diagnóstico da tela de Administração do Servidor;
- Recomenda-se que rotinas que demandam muito tempo de processamento sejam realizadas de maneira agendada, em momentos de menor uso do sistema;
