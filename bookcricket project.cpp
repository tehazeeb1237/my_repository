#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int toss();
int play_game(int player);
int generate_random_number();
void print_scoreboard(int player1_score, int player2_score);

int main() {
    int toss_result, player_turn, player1_score = 0, player2_score = 0;

    printf("Welcome to Book Cricket Game!\n\n");

    toss_result = toss();
    if (toss_result == 1) {
        printf("Player 1 won the toss and will go first.\n");
        player_turn = 1;
    } else {
        printf("Player 2 won the toss and will go first.\n");
        player_turn = 2;
    }

   
    while (player1_score == 0 || player2_score == 0) {
        if (player_turn == 1) {
            player1_score += play_game(player_turn);
            print_scoreboard(player1_score, player2_score);
            player_turn = 2;
        } else {
            player2_score += play_game(player_turn);
            print_scoreboard(player1_score, player2_score);
            player_turn = 1;
        }
    }

    // Determine the winner
    printf("\n\n");
    if (player1_score > player2_score) {
        printf("Player 1 wins by %d runs!\n", player1_score - player2_score);
    } else {
        printf("Player 2 wins by %d runs!\n", player2_score - player1_score);
    }

    return 0;
}


int toss() {
    int toss_result;
    printf("Tossing the coin... ");
    srand(time(NULL));
    toss_result = rand() % 2 + 1;
    if (toss_result == 1) {
        printf("It's heads!\n");
    } else {
        printf("It's tails!\n");
    }
    return toss_result;
}


int play_game(int player) {
    int score = 0, runs;

    printf("\n\nPlayer %d, it's your turn to bat.\n", player);
    printf("Press enter to start batting...");
    getchar();

    do {
        runs = generate_random_number();
        printf("You scored %d runs.\n", runs);
        if (runs > 0) {
            score += runs;
        } else {
            printf("You're out!\n");
            break;
        }
        printf("Your current score is %d.\n", score);
        printf("Press enter to continue batting or type 0 to end your innings...");
    } while (getchar() != '0');

    printf("Your innings has ended with a total score of %d.\n", score);
    return score;
}


int generate_random_number() {
    srand(time(NULL));
    return rand() % 10;
}
void print_scoreboard(int player1_score, int player2_score) {
    printf("\n\nScoreboard:\n");
    printf("Player 1: %d runs\n", player1_score);
    printf("Player 2: %d runs\n", player2_score);
}
