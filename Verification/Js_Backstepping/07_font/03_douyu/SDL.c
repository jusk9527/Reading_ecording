#include <stdio.h>
#include <SDL2/SDL.h>
#include <SDL2/SDL_ttf.h>

#include <SDL2/SDL_image.h>

int
main(void)
{
  if(TTF_Init() == -1) {
    printf("error: %s\n", TTF_GetError());
    return 1;
  }

  TTF_Font *font = TTF_OpenFont("mpepc5unpb.woff", 50);
  if(font == NULL) {
    printf("error: %s\n", TTF_GetError());
    return 1;
  }

  SDL_Color black = { 0x00, 0x00, 0x00 };
  SDL_Surface *surface = TTF_RenderText_Solid(font, "0123456789", black);
  if(surface == NULL) {
    printf("error: %s\n", TTF_GetError());
    return 1;
  }

  IMG_SavePNG(surface, "test.png");
  return 0;
}