<template>
  <v-app>
    <v-form v-model="valid">
      <v-container>
        <v-row>
          <v-col>
            <v-text-field
              v-model="id"
              :rules="rules"
              maxlength="20"
              counter
              label="아이디"
              clearable
              required
            />
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <v-text-field
              v-model="password"
              :rules="rules"
              maxlength="20"
              counter
              type="password"
              label="비밀번호"
              clearable
              required
            />
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <v-btn
              type="submit"
            >
              로그인
            </v-btn>
          </v-col>
        </v-row>
      </v-container>
    </v-form>
  </v-app>
</template>

<script>
  export default {
    name: 'Login',

    components: {
    },

    data: () => ({
      id: '',
      password: '',
      valid: false,
      rules: [
        value => !!value || '',
        value => (value && value.length <= 20) || '20자 제한',
      ],
    }),
  }
</script>
