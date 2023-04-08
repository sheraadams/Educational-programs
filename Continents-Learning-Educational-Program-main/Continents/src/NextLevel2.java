import java.awt.BorderLayout;
import java.awt.CardLayout;
import java.awt.Color;
import java.awt.Component;
import java.awt.EventQueue;
import java.awt.FlowLayout;
import java.awt.HeadlessException;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;

public class NextLevel extends JFrame {
    private JPanel slidePane;
    private JPanel textPane;
    private JPanel buttonPane;
    private CardLayout card;
    private CardLayout cardText;
    private JButton btnPrev;
    private JButton btnNext;
    private JLabel lblSlide;
    private JLabel lblTextArea;

    public NextLevel() throws HeadlessException {
        this.initComponent();
    }

    private void initComponent() {
        this.card = new CardLayout();
        this.cardText = new CardLayout();
        this.slidePane = new JPanel();
        this.textPane = new JPanel();
        this.textPane.setBackground(Color.WHITE);
        this.textPane.setBounds(5, 470, 790, 50);
        this.textPane.setVisible(true);
        this.buttonPane = new JPanel();
        this.btnPrev = new JButton();
        this.btnNext = new JButton();
        this.lblSlide = new JLabel();
        this.lblTextArea = new JLabel();
        this.setSize(800, 600);
        this.setLocationRelativeTo((Component)null);
        this.setTitle("Text Game");
        this.getContentPane().setLayout(new BorderLayout(10, 50));
        this.setDefaultCloseOperation(3);
        this.slidePane.setLayout(this.card);
        this.textPane.setLayout(this.cardText);

        for(int i = 1; i <= 5; ++i) {
            this.lblSlide = new JLabel();
            this.lblTextArea = new JLabel();
            this.lblSlide.setText(this.getResizeIcon(i));
            this.lblTextArea.setText(this.getTextDescription(i));
            this.slidePane.add(this.lblSlide, "card" + i);
            this.textPane.add(this.lblTextArea, "cardText" + i);
        }

        this.getContentPane().add(this.slidePane, "Center");
        this.getContentPane().add(this.textPane, "South");
        this.buttonPane.setLayout(new FlowLayout(1, 20, 10));
        this.btnPrev.setText("Previous");
        this.btnPrev.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                NextLevel.this.goPrevious();
            }
        });
        this.buttonPane.add(this.btnPrev);
        this.btnNext.setText("    Next    ");
        this.btnNext.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                NextLevel.this.goNext();
            }
        });
        this.buttonPane.add(this.btnNext);
        this.getContentPane().add(this.buttonPane, "South");
    }

    private void goPrevious() {
        this.card.previous(this.slidePane);
        this.cardText.previous(this.textPane);
    }

    private void goNext() {
        this.card.next(this.slidePane);
        this.cardText.next(this.textPane);
    }

    private String getResizeIcon(int i) {
        String image = "";
        if (i == 1) {
            image = "<html><body><img width= '800' height='500' src='" + this.getClass().getResource("/resources/bahamas.jpg") + "'</body></html>";
        } else if (i == 2) {
            image = "<html><body><img width= '800' height='500' src='" + this.getClass().getResource("/resources/sedona.jpg") + "'</body></html>";
        } else if (i == 3) {
            image = "<html><body><img width= '800' height='500' src='" + this.getClass().getResource("/resources/costarica.jpg") + "'</body></html>";
        } else if (i == 4) {
            image = "<html><body><img width= '800' height='500' src='" + this.getClass().getResource("/resources/egypt.jpg") + "'</body></html>";
        } else if (i == 5) {
            image = "<html><body><img width= '800' height='500' src='" + this.getClass().getResource("/resources/grandcanyon.jpg") + "'</body></html>";
        }

        return image;
    }

    private String getTextDescription(int i) {
        String text = "";
        if (i == 1) {
            text = "<html><body><font size='5'>Dungeon</font> <br>You have found a knife. </body></html>";
        } else if (i == 2) {
            text = "<html><body><font size='5'>Lair</font> <br> You had better run.</body></html>";
        } else if (i == 3) {
            text = "<html><body><font size='5'>Alley</font> <br>You have found a map.</body></html>";
        } else if (i == 4) {
            text = "<html><body><font size='5'>Tower</font> <br>You have found a sword.</body></html>";
        } else if (i == 5) {
            text = "<html><body><font size='5'>5Strand</font> <br>You have found a potion.</body></html>";
        }

        return text;
    }

    public static void main(String[] args) {
        EventQueue.invokeLater(new Runnable() {
            public void run() {
                NextLevel ss = new NextLevel();
                ss.setVisible(true);
            }
        });
    }
}
