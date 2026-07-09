// pacman -S mingw-w64-x86_64-SDL2
// gcc main.c -o main $(pkg-config --libs --cflags sdl2)

#include <SDL2/SDL.h>
#include <stdbool.h>

int main(int argc, char *argv[]) {
    (void)argc;
    (void)argv;

    SDL_Init(SDL_INIT_VIDEO);

    SDL_Window *window = SDL_CreateWindow(
        "SDL2 Kickstart",
        SDL_WINDOWPOS_CENTERED,
        SDL_WINDOWPOS_CENTERED,
        800,
        600,
        SDL_WINDOW_SHOWN
    );

    SDL_Renderer *renderer = SDL_CreateRenderer(
        window,
        -1,
        SDL_RENDERER_ACCELERATED
    );

    bool running = true;
    SDL_Event event;

    int x = 100;
    int y = 100;

    while (running) {
        while (SDL_PollEvent(&event)) {
            if (event.type == SDL_QUIT) {
                running = false;
            }

            if (event.type == SDL_KEYDOWN) {
                if (event.key.keysym.sym == SDLK_ESCAPE) {
                    running = false;
                }

                if (event.key.keysym.sym == SDLK_LEFT) {
                    x -= 10;
                }

                if (event.key.keysym.sym == SDLK_RIGHT) {
                    x += 10;
                }

                if (event.key.keysym.sym == SDLK_UP) {
                    y -= 10;
                }

                if (event.key.keysym.sym == SDLK_DOWN) {
                    y += 10;
                }
            }
        }

        SDL_SetRenderDrawColor(renderer, 20, 20, 30, 255);
        SDL_RenderClear(renderer);

        SDL_Rect player = { x, y, 50, 50 };

        SDL_SetRenderDrawColor(renderer, 80, 200, 120, 255);
        SDL_RenderFillRect(renderer, &player);

        SDL_RenderPresent(renderer);

        SDL_Delay(16);
    }

    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();

    return 0;
}
