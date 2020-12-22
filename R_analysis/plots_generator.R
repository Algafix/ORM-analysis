library(ggplot2)
library(scales)

#### Data Reading ####

data_cookies = read.csv("../cookies_report.csv", 
                        colClasses=c('integer','character', 'integer','integer','logical'))
head(data_cookies)

cookies_clicked = subset(data_cookies, clicked == TRUE)
cookies_not_clicked = subset(data_cookies, clicked == FALSE)


#### Pie chart clicked vs not ####

domains_clicked <- data.frame(
  clicked = c("Accepted", "Not asked/Not accepted"),
  n = c(nrow(cookies_clicked), nrow(cookies_not_clicked)),
  prop = c(nrow(cookies_clicked)*100/nrow(data_cookies),
           nrow(cookies_not_clicked)*100/nrow(data_cookies))
)

domains_clicked

blank_theme <- theme_minimal()+
  theme(
    axis.title.x = element_blank(),
    axis.title.y = element_blank(),
    panel.border = element_blank(),
    panel.grid=element_blank(),
    axis.ticks = element_blank(),
    plot.title=element_text(size=20, face="bold"),
    text = element_text(size=30)
  )

domains_clicked$label_ypos = 20 + cumsum(domains_clicked$prop)- domains_clicked$prop/2

bp <- ggplot(domains_clicked, aes(x="", y=prop, fill=clicked))+
  geom_bar(width = 1, stat = "identity")

pie <- bp + coord_polar("y", start=0)

pie + scale_fill_brewer("Cookies", palette = "Set2") + blank_theme +
  theme(axis.text.x=element_blank())+
  geom_text(aes(y = rev(label_ypos), 
                label = percent(prop/100)), size=10)


#### Pie chart same vs more cookies ####

same_cookies <- subset(cookies_clicked, cookies_default + cookies_accepted != 0 
                       & cookies_default >= cookies_accepted)
more_cookies <- subset(cookies_clicked, !(domain_ID %in% same_cookies$domain_ID))

cookies_after_click <- data.frame(
  cookies = c("Same cookies", "More cookies"),
  n = c(nrow(same_cookies), nrow(more_cookies)),
  prop = c(nrow(same_cookies)*100/nrow(cookies_clicked),
           nrow(more_cookies)*100/nrow(cookies_clicked))
)

cookies_after_click

blank_theme <- theme_minimal()+
  theme(
    axis.title.x = element_blank(),
    axis.title.y = element_blank(),
    panel.border = element_blank(),
    panel.grid=element_blank(),
    axis.ticks = element_blank(),
    plot.title=element_text(size=20, face="bold"),
    text = element_text(size=30)
  )

cookies_after_click$label_ypos = (0 + cumsum(cookies_after_click$prop) 
                                  - cookies_after_click$prop/2)

bp_cookies_a_click <- ggplot(cookies_after_click, aes(x="", y=prop, fill=cookies))+
  geom_bar(width = 1, stat = "identity")

pie_cookies_a_click <- bp_cookies_a_click + coord_polar("y", start=0)

pie_cookies_a_click + scale_fill_brewer("Number of cookies", palette = "Set2") + blank_theme +
  theme(axis.text.x=element_blank())+
  geom_text(aes(y = label_ypos, 
                label = percent(prop/100)), size=10)


#### How many cookies by saying yes ####

number_cookies_default <- sum(cookies_clicked$cookies_default)
number_cookies_default

number_cookies_accepting <- sum(cookies_clicked$cookies_accepted)
number_cookies_accepting

number_of_cookies <- data.frame(
  action = c("Not interacting", "Accepting"),
  n = c(number_cookies_default, number_cookies_accepting)
)

number_of_cookies

number_cookies_plot <- ggplot(data=number_of_cookies, aes(x=action, y=n, fill=action)) +
  geom_bar(stat="identity", width=0.5)+
  geom_text(aes(label=n), vjust=-0.3, size=5)+
  theme_minimal()+
  labs(fill = "Action:")+
  scale_y_continuous(name="Number of cookies")+
  scale_x_discrete(name="Action performed")+
  theme(text = element_text(size=20))

number_cookies_plot



















